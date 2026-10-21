# Troca o compacto FECHADO gerado por IA (deformado) pela tampa REAL em perspectiva.
# 1) apaga o fechado falso: preenche o polígono interpolando o fundo de cada linha (fundo escuro liso)
# 2) aplica a textura real da tampa (lid_texture.py) num quadrilátero, com espessura, rim light,
#    sombra de contato e reflexo na superfície.
# uso: closed_lid_place.py base.png lid.png out.png '{"erase":[[x,y],...],"face":[TL,TR,BR,BL],"depth":[dx,dy],"rim":[r,g,b],"refl":0.18}'
import sys, json
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

base_p, lid_p, out_p, cfg = sys.argv[1], sys.argv[2], sys.argv[3], json.loads(sys.argv[4])
img = Image.open(base_p).convert('RGB'); W, H = img.size
arr = np.array(img).astype(np.float32)

def poly_mask(pts, blur=0):
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).polygon([tuple(p) for p in pts], fill=255)
    return m.filter(ImageFilter.GaussianBlur(blur)) if blur else m

# 1) erase
if cfg.get('erase'):
    m = np.array(poly_mask(cfg['erase'])) > 0
    fill = arr.copy()
    for y in np.where(m.any(1))[0]:
        xs = np.where(m[y])[0]; x0, x1 = max(xs[0] - 6, 0), min(xs[-1] + 6, W - 1)
        L = arr[y, max(x0 - 12, 0):x0].mean(0); R = arr[y, x1:min(x1 + 12, W)].mean(0)
        t = np.linspace(0, 1, x1 - x0 + 1)[:, None]
        fill[y, x0:x1 + 1] = L * (1 - t) + R * t
    fill = np.array(Image.fromarray(fill.clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))).astype(np.float32)
    fill += np.random.default_rng(1).normal(0, 1.2, fill.shape)       # grão de foto
    soft = np.array(poly_mask(cfg['erase'], 4)).astype(np.float32)[..., None] / 255
    arr = arr * (1 - soft) + fill * soft

def coeffs(dst, src):
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()

def warp(tex, quad):
    w, h = tex.size
    return tex.transform((W, H), Image.PERSPECTIVE, coeffs(quad, [(0, 0), (w, 0), (w, h), (0, h)]), Image.BICUBIC)

lid = Image.open(lid_p).convert('RGBA')
face = cfg['face']; dx, dy = cfg.get('depth', [0, 0])
TL, TR, BR, BL = face
out = Image.fromarray(arr.clip(0, 255).astype(np.uint8))

# sombra de contato sob a aresta inferior
sh = Image.new('L', (W, H), 0)
ImageDraw.Draw(sh).polygon([tuple(BL), tuple(BR), (BR[0] + dx, BR[1] + dy + 10), (BL[0] + dx, BL[1] + dy + 10)], fill=255)
sh = sh.filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * 0.8))
out = Image.composite(Image.new('RGB', (W, H), (0, 0, 0)), out, sh)

# reflexo na superfície (tampa espelhada para baixo, esmaecendo)
if cfg.get('refl'):
    rq = [BL, BR, [BR[0], 2 * BR[1] - TR[1]], [BL[0], 2 * BL[1] - TL[1]]]
    r = warp(lid.transpose(Image.FLIP_TOP_BOTTOM), [rq[3], rq[2], rq[1], rq[0]][::-1][::-1])
    r = warp(lid.transpose(Image.FLIP_TOP_BOTTOM), [[BL[0], 2 * BL[1] - TL[1]], [BR[0], 2 * BR[1] - TR[1]], BR, BL])
    ra = np.array(r.getchannel('A')).astype(np.float32)
    yy = np.arange(H)[:, None]; top = min(BL[1], BR[1]); span = max(abs(BL[1] - TL[1]), 1)
    fade = np.clip(1 - (yy - top) / (span * 0.45), 0, 1) * cfg['refl']
    r.putalpha(Image.fromarray((ra * fade).clip(0, 255).astype(np.uint8)))
    out.paste(r.filter(ImageFilter.GaussianBlur(2.5)), (0, 0), r.filter(ImageFilter.GaussianBlur(2.5)))

# espessura: aresta de cima e lateral direita (preto brilhante com leve gradiente)
d = ImageDraw.Draw(out)
d.polygon([tuple(TL), tuple(TR), (TR[0] + dx, TR[1] + dy), (TL[0] + dx, TL[1] + dy)], fill=(22, 20, 21))
d.polygon([tuple(TR), tuple(BR), (BR[0] + dx, BR[1] + dy), (TR[0] + dx, TR[1] + dy)], fill=(10, 9, 10))

# face com a tampa real
f = warp(lid, face)
fa = f.getchannel('A')
out.paste(f, (0, 0), fa)

# brilho especular suave (diagonal) só na face, sem tocar no logo de forma forte
yy, xx = np.mgrid[0:H, 0:W]
cx, cy = (TL[0] + BR[0]) / 2, (TL[1] + BR[1]) / 2
band = np.exp(-(((xx - cx) * 0.55 + (yy - cy) * 0.85 + (BR[1] - TL[1]) * 0.25) / ((BR[0] - TL[0]) * 0.18)) ** 2) * 16
o = np.array(out).astype(np.float32); fam = np.array(fa).astype(np.float32)[..., None] / 255
o += band[..., None] * fam * np.array([1.0, 0.95, 0.9])
out = Image.fromarray(o.clip(0, 255).astype(np.uint8))

# rim light quente nas arestas
rim = tuple(cfg.get('rim', [190, 120, 80]))
e = Image.new('L', (W, H), 0); de = ImageDraw.Draw(e)
de.line([tuple(BL), tuple(TL), (TL[0] + dx, TL[1] + dy), (TR[0] + dx, TR[1] + dy)], fill=200, width=2)
de.line([tuple(TL), tuple(TR)], fill=110, width=2)
de.line([(TR[0] + dx, TR[1] + dy), (BR[0] + dx, BR[1] + dy)], fill=150, width=2)
e = e.filter(ImageFilter.GaussianBlur(1.2))
out = Image.composite(Image.new('RGB', (W, H), rim), out, e.point(lambda v: int(v * 0.55)))
out.save(out_p); print('ok', out_p)
