#!/usr/bin/env python3
"""Composite-first product lock.

Recorta os packshots REAIS (assets/products/{handle}/01.*) e posiciona cada
peça (corpo/tampa) num canvas segundo um layout JSON. Nenhum pixel de produto
é gerado por IA -> logo, lettering e formato são 100% os oficiais.

Uso:
    python3 pipeline/scripts/composite_hero.py layout.json out.png

Layout JSON:
{
  "canvas": [1080, 1920],
  "background": "#050505",
  "glows": [{"center": [x, y], "radius": r, "color": "#1c1c1c"}],
  "items": [
    {"packshot": "assets/products/intense-eye-black/01.png",
     "part": 0,            # 0 = maior componente (corpo), 1 = segundo (tampa)...
     "tip": [x, y],        # opcional: ponto onde fica a ponta (topo do packshot)
     "center": [x, y],     # alternativa a tip: centro da peça
     "dir": [dx, dy],      # direção para onde a ponta/topo aponta
     "scale": 1.15,
     "shadow": true}
  ]
}
"""
import json
import math
import sys

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def cutout_parts(path):
    """Separa o produto do fundo off-white e devolve as peças (RGBA), maior primeiro."""
    rgb = np.asarray(Image.open(path).convert("RGB")).astype(np.float32)
    lum = rgb @ np.array([0.299, 0.587, 0.114], np.float32)
    # packshots têm fundo claro com sombra suave (~215-245) colada na peça:
    # limiar baixo de luminância descarta a sombra; brilhos/lettering internos
    # são recuperados pelo fill_holes.
    hard = ndimage.binary_fill_holes(lum < 160)
    hard = ndimage.binary_opening(hard, iterations=1)
    # borda: 1px de alpha parcial proporcional à luminância (anti-alias real)
    outer = ndimage.binary_dilation(hard, iterations=1) & ~hard
    alpha = hard.astype(np.float32) + outer * np.clip((215 - lum) / 160.0, 0, 1)
    # descontaminação: borda externa + 1px interno recebem a cor interna mais próxima
    core = ndimage.binary_erosion(hard, iterations=1)
    ring = (outer | hard) & ~core
    _, (iy, ix) = ndimage.distance_transform_edt(~core, return_indices=True)
    color = np.where(ring[..., None], rgb[iy, ix], rgb)

    labels, n = ndimage.label(ndimage.binary_dilation(hard, iterations=1))
    sizes = ndimage.sum(np.ones_like(labels), labels, range(1, n + 1))
    order = np.argsort(sizes)[::-1]
    parts = []
    for idx in order:
        if sizes[idx] < 2000:
            continue
        m = labels == idx + 1
        ys, xs = np.where(m)
        y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
        a = np.where(m, alpha, 0)[y0:y1, x0:x1]
        c = color[y0:y1, x0:x1]
        rgba = np.dstack([c, a * 255]).clip(0, 255).astype(np.uint8)
        parts.append(Image.fromarray(rgba, "RGBA"))
    return parts


def place(canvas, piece, item):
    s = item.get("scale", 1.0)
    piece = piece.resize((round(piece.width * s), round(piece.height * s)), Image.LANCZOS)
    dx, dy = item["dir"]
    # peça original aponta para cima (0,-1); ângulo em coords de imagem (y para baixo)
    target = math.degrees(math.atan2(dy, dx))
    rot = -(target - (-90))  # PIL.rotate é anti-horário visual
    h = piece.height
    rotated = piece.rotate(rot, resample=Image.BICUBIC, expand=True)
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    if "tip" in item:
        cx = item["tip"][0] - ux * h / 2
        cy = item["tip"][1] - uy * h / 2
    else:
        cx, cy = item["center"]
    pos = (round(cx - rotated.width / 2), round(cy - rotated.height / 2))
    if item.get("shadow", True):
        a = rotated.split()[3]
        sh = Image.new("RGBA", rotated.size, (0, 0, 0, 0))
        sh.putalpha(a.point(lambda v: int(v * 0.85)))
        sh = sh.filter(ImageFilter.GaussianBlur(18))
        canvas.alpha_composite(sh, (pos[0] + 14, pos[1] + 22))
    canvas.alpha_composite(rotated, pos)


def render(layout):
    W, H = layout["canvas"]
    base = np.zeros((H, W, 3), np.float32) + np.array(hex_rgb(layout.get("background", "#050505")), np.float32)
    yy, xx = np.mgrid[0:H, 0:W]
    for g in layout.get("glows", []):
        gx, gy = g["center"]
        r = g["radius"]
        w = np.exp(-(((xx - gx) ** 2 + (yy - gy) ** 2) / (2 * (r / 2) ** 2)))[..., None]
        col = np.array(hex_rgb(g["color"]), np.float32)
        base = base * (1 - w) + np.maximum(base, col) * w
    canvas = Image.fromarray(base.clip(0, 255).astype(np.uint8)).convert("RGBA")
    cache = {}
    for item in layout["items"]:
        p = item["packshot"]
        if p not in cache:
            cache[p] = cutout_parts(p)
        place(canvas, cache[p][item.get("part", 0)], item)
    return canvas.convert("RGB")


if __name__ == "__main__":
    layout = json.load(open(sys.argv[1]))
    render(layout).save(sys.argv[2])
    print("ok", sys.argv[2])
