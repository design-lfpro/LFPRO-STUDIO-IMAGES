#!/usr/bin/env python3
"""Composite deterministico: packshot real (fundo off-white) -> hero dark-studio.

Fallback ZERO RISCO DE IA pra still hero. Usar quando:
- Sofia (still-engineer) decide strategy = "packshot-composite" pro beat
- Rita Still Verifier decide `FALLBACK_COMPOSITE` depois de 2 re-rolls de still

Como funciona (sem generative AI, so processamento de imagem):
1. Resolve o packshot oficial `assets/products/{handle}/01.*` (via resolve_packshot).
2. Estima a cor do fundo off-white amostrando pixels perto da borda.
3. Recorta o produto do fundo com flood fill a partir das bordas (mascara alpha
   calculada em baixa resolucao pra performance, depois upscale com blur —
   isso tambem produz uma borda suave/anti-aliased natural).
4. Compoe o produto (packaging 1:1, zero deformacao) sobre um fundo dark-studio
   gradiente (charcoal -> preto, conforme brand-dna) com sombra de contato soft.

Logo, forma do pote, cor do produto: identicos ao packshot real (nao passam
por nenhum modelo generativo) — resolve por definicao qualquer risco de
"produto divergente do real" nesse still.

Limitacao conhecida: em companions bem translucidos do packshot (swatch de
po solto, stroke de creme com borda soft) pode sobrar uma leve franja clara
no recorte — o corpo do produto (pote/tubo/tampa/logo) fica limpo, só o
elemento decorativo ao redor pode precisar de --thresh/--margin ajustado ou
crop manual do `--source` se for pro still final (nao bloqueia o gate da
Rita, que avalia packaging, nao o swatch solto).

Uso:
    python3 pipeline/scripts/composite_dark_hero.py po-soft-eye-claro
    python3 pipeline/scripts/composite_dark_hero.py po-soft-eye-claro \
        --out output/20260904-1200/stills/start-composite.png --width 1080 --height 1920

Requer Pillow + numpy (pip install pillow numpy).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolve_packshot import resolve  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]


def _hex(color: str) -> tuple[int, int, int]:
    color = color.lstrip("#")
    return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def _border_bg_color(im: Image.Image, samples: int = 24) -> tuple[int, int, int]:
    """Amostra pixels perto da borda pra estimar a cor do fundo off-white do site."""
    w, h = im.size
    px = im.convert("RGB").load()
    pts = []
    step_x = max(1, w // samples)
    step_y = max(1, h // samples)
    for x in range(0, w, step_x):
        pts.append(px[x, 1])
        pts.append(px[x, h - 2])
    for y in range(0, h, step_y):
        pts.append(px[1, y])
        pts.append(px[w - 2, y])
    r = sum(p[0] for p in pts) // len(pts)
    g = sum(p[1] for p in pts) // len(pts)
    b = sum(p[2] for p in pts) // len(pts)
    return (r, g, b)


def _cutout_mask(im: Image.Image, bg: tuple[int, int, int], thresh: int, work_size: int = 480) -> Image.Image:
    """Mascara alpha (255=produto, 0=fundo).

    Flood fill a partir de todas as bordas em resolucao reduzida (rapido e
    determinístico), so remove regiao **contigua** a borda que bater com a
    cor do fundo — nao come partes claras do produto (puff, pote translucido)
    que nao estejam coladas na borda. Upscale final com blur = feather natural.
    """
    rgb = im.convert("RGB")
    small = ImageOps.contain(rgb, (work_size, work_size))
    sw, sh = small.size
    mask = Image.new("L", small.size, 255)  # 255 = mantem (produto)
    px = small.load()
    mpx = mask.load()
    limit = thresh * 3  # soma das 3 distancias de canal (manhattan)

    visited = bytearray(sw * sh)

    def idx(x: int, y: int) -> int:
        return y * sw + x

    stack: list[tuple[int, int]] = []
    for x in range(sw):
        for y in (0, sh - 1):
            i = idx(x, y)
            if not visited[i]:
                r, g, b = px[x, y]
                if abs(r - bg[0]) + abs(g - bg[1]) + abs(b - bg[2]) <= limit:
                    visited[i] = 1
                    stack.append((x, y))
    for y in range(sh):
        for x in (0, sw - 1):
            i = idx(x, y)
            if not visited[i]:
                r, g, b = px[x, y]
                if abs(r - bg[0]) + abs(g - bg[1]) + abs(b - bg[2]) <= limit:
                    visited[i] = 1
                    stack.append((x, y))

    while stack:
        x, y = stack.pop()
        mpx[x, y] = 0
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < sw and 0 <= ny < sh:
                ni = idx(nx, ny)
                if not visited[ni]:
                    r, g, b = px[nx, ny]
                    if abs(r - bg[0]) + abs(g - bg[1]) + abs(b - bg[2]) <= limit:
                        visited[ni] = 1
                        stack.append((nx, ny))

    # erode antes de suavizar: o blur simetrico "reinfla" a mascara de volta pra
    # fora, e como os pixels ali fora sao 100% fundo (alpha=0 antes do blur),
    # decontaminar essa faixa so devolve a propria cor do fundo com alpha
    # parcial -> halo claro. Erodir 2px primeiro garante que o blur nunca
    # espalha alpha além do contorno real do produto.
    mask = mask.filter(ImageFilter.MinFilter(5))  # erode ~2px
    mask = mask.filter(ImageFilter.GaussianBlur(radius=1))
    mask = mask.resize(im.size, Image.LANCZOS)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=1))
    return mask


def _decontaminate(rgb: Image.Image, mask: Image.Image, bg: tuple[int, int, int]) -> Image.Image:
    """Remove o resíduo do fundo off-white que vaza nos pixels semi-transparentes
    da borda (halo/fringe claro), fazendo o "unmix" do alpha compositing:
    pixel = alpha*fg + (1-alpha)*bg  =>  fg = (pixel - (1-alpha)*bg) / alpha
    Sem isso o cutout fica com uma auréola branca-esverdeada contra o fundo dark.
    """
    arr = np.asarray(rgb.convert("RGB"), dtype=np.float32)
    a = np.asarray(mask, dtype=np.float32) / 255.0
    a3 = a[..., None]
    bg_arr = np.array(bg, dtype=np.float32)
    fg = (arr - (1.0 - a3) * bg_arr) / np.clip(a3, 1e-3, 1.0)
    fg = np.clip(fg, 0, 255)
    # em regiao muito translucida (pó/swatch soltando particulas, alpha baixo) o
    # unmix "explode" e cria franja — amortece de volta pra cor original nesses
    # trechos, só confia no unmix total onde a mascara já é sólida (produto real)
    damp = np.clip(a3 / 0.5, 0.0, 1.0)
    fg = fg * damp + arr * (1.0 - damp)
    rgba = np.concatenate([fg, a3 * 255.0], axis=-1).astype(np.uint8)
    return Image.fromarray(rgba, mode="RGBA")


def _dark_studio_bg(size: tuple[int, int], top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    w, h = size
    bg = Image.new("RGB", size, bottom)
    draw = ImageDraw.Draw(bg)
    for y in range(h):
        t = y / max(1, h - 1)
        row = tuple(int(top[c] + (bottom[c] - top[c]) * t) for c in range(3))
        draw.line([(0, y), (w, y)], fill=row)
    return bg


def _add_contact_shadow(canvas: Image.Image, bbox: tuple[int, int, int, int], opacity: int = 120) -> None:
    x0, y0, x1, y1 = bbox
    w = x1 - x0
    h_shadow = max(16, int((y1 - y0) * 0.10))
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(shadow)
    cy = y1 - int(h_shadow * 0.35)
    draw.ellipse([x0 + w * 0.10, cy, x1 - w * 0.10, cy + h_shadow], fill=(0, 0, 0, opacity))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=max(8, w // 22)))
    canvas.alpha_composite(shadow)


def composite(
    handle: str,
    out_path: Path,
    *,
    width: int = 1080,
    height: int = 1920,
    source: str | None = None,
    bg_top: str = "1a1a1a",
    bg_bottom: str = "0a0a0a",
    margin: float = 0.14,
    thresh: int = 30,
) -> Path:
    src_path = Path(source) if source else resolve(handle)
    packshot = Image.open(src_path).convert("RGB")

    bg_color = _border_bg_color(packshot)
    alpha_mask = _cutout_mask(packshot, bg_color, thresh=thresh)
    product_rgba = _decontaminate(packshot, alpha_mask, bg_color)

    bbox = alpha_mask.getbbox()
    if bbox:
        pad = int(0.03 * max(product_rgba.size))
        bbox = (
            max(0, bbox[0] - pad),
            max(0, bbox[1] - pad),
            min(product_rgba.width, bbox[2] + pad),
            min(product_rgba.height, bbox[3] + pad),
        )
        product_rgba = product_rgba.crop(bbox)

    canvas = _dark_studio_bg((width, height), _hex(bg_top), _hex(bg_bottom)).convert("RGBA")

    max_w = int(width * (1 - margin))
    max_h = int(height * (1 - margin))
    scale = min(max_w / product_rgba.width, max_h / product_rgba.height, 1.0) or 1.0
    new_size = (max(1, int(product_rgba.width * scale)), max(1, int(product_rgba.height * scale)))
    product_rgba = product_rgba.resize(new_size, Image.LANCZOS)

    px = (width - product_rgba.width) // 2
    py = int(height * 0.50 - product_rgba.height * 0.52)
    py = max(0, min(py, height - product_rgba.height))

    _add_contact_shadow(canvas, (px, py, px + product_rgba.width, py + product_rgba.height))
    canvas.alpha_composite(product_rgba, (px, py))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(out_path, quality=95)
    return out_path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("handle", help="handle do produto (ex. po-soft-eye-claro)")
    ap.add_argument("--out", help="path de saida (default: output/composites/{handle}-dark.png)")
    ap.add_argument("--source", help="override do packshot (default: resolve via resolve_packshot.py)")
    ap.add_argument("--width", type=int, default=1080)
    ap.add_argument("--height", type=int, default=1920)
    ap.add_argument("--bg-top", default="1a1a1a", help="hex do topo do gradiente (ver brand-dna 00, charcoal)")
    ap.add_argument("--bg-bottom", default="0a0a0a", help="hex da base do gradiente (ver brand-dna 00, preto)")
    ap.add_argument("--margin", type=float, default=0.14, help="margem livre ao redor do produto (0-1)")
    ap.add_argument("--thresh", type=int, default=30, help="tolerancia de cor pro flood fill do fundo off-white")
    args = ap.parse_args()

    out_path = Path(args.out) if args.out else ROOT / "output" / "composites" / f"{args.handle}-dark.png"
    result = composite(
        args.handle,
        out_path,
        width=args.width,
        height=args.height,
        source=args.source,
        bg_top=args.bg_top,
        bg_bottom=args.bg_bottom,
        margin=args.margin,
        thresh=args.thresh,
    )
    print(result)


if __name__ == "__main__":
    main()
