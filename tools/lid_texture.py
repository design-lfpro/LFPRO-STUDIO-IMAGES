# Reconstrói a tampa FECHADA real (frontal) a partir do packshot oficial.
# A foto do site esconde ~1/3 direito da tampa atrás da paleta aberta; a tampa é preta lisa,
# então completamos espelhando a borda esquerda (canto arredondado incluso). Logo/wordmark = pixels reais.
# uso: lid_texture.py packshot.png out.png
import sys
import numpy as np
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = np.array(Image.open(src).convert('RGB')).astype(np.float32)
X0, X1, Y0, Y1 = 187, 466, 368, 695      # parte visível da tampa no 01.png (1080²)
CX = 399                                  # centro do monograma = centro da tampa
W = 2 * (CX - X0)                         # ≈ 424 px → proporção ≈ 1,3:1
vis = im[Y0:Y1, X0:X1]
lid = np.zeros((Y1 - Y0, W, 3), np.float32)
lid[:, :X1 - X0] = vis
n = W - (X1 - X0)
lid[:, X1 - X0:] = vis[:, :n][:, ::-1]    # espelho da borda esquerda → borda direita
# alfa: cantos arredondados (raio ~6px) a partir do próprio recorte espelhado
a = np.full(lid.shape[:2], 255, np.uint8)
r = 6
for (cy, cx) in [(r, r), (r, W - 1 - r), (lid.shape[0] - 1 - r, r), (lid.shape[0] - 1 - r, W - 1 - r)]:
    yy, xx = np.mgrid[0:lid.shape[0], 0:W]
    corner = ((yy < r) | (yy > lid.shape[0] - 1 - r)) & ((xx < r) | (xx > W - 1 - r))
    d = np.sqrt((yy - cy) ** 2 + (xx - cx) ** 2)
    a[corner & (d > r) & (np.abs(yy - cy) <= r) & (np.abs(xx - cx) <= r)] = 0
o = Image.fromarray(np.clip(lid, 0, 255).astype(np.uint8)); o.putalpha(Image.fromarray(a))
o.save(out); print('ok', o.size)
