import sys, random
from PIL import Image, ImageFilter, ImageDraw, ImageChops
import numpy as np
src, out, prev = sys.argv[1], sys.argv[2], sys.argv[3]
amp, sheen, spark = float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
im = Image.open(src).convert('RGB'); A = np.asarray(im).astype(np.float32)
BM = (622, 608, 727, 689)   # rosé cobre (cintilante) – fonte de textura
BR = (737, 608, 844, 689)   # pêssego nude – alvo
W, H = BR[2]-BR[0], BR[3]-BR[1]
# textura: high-pass da luminância do godet cintilante vizinho
L = np.asarray(im.crop(BM).convert('L').resize((W, H), Image.LANCZOS)).astype(np.float32)
blur = np.asarray(Image.fromarray(L.astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))).astype(np.float32)
hp = L - blur; hp = hp / (hp.std() + 1e-6)
# cor alvo (pó real, levemente ajustado à luz da foto)
target = np.array([0xE6, 0xB1, 0x9C], np.float32)
yy, xx = np.mgrid[0:H, 0:W]
# reflexo perolado: diagonal mais clara no topo-esquerda + leve banda de brilho
g = 1 - (xx / W * 0.5 + yy / H * 0.5)
band = np.exp(-((xx/W - yy/H*0.6 - 0.25)**2) / 0.02)
lum = hp * amp + (g - 0.5) * sheen + band * sheen * 0.6
rng = np.random.default_rng(7)
sp = (rng.random((H, W)) < spark).astype(np.float32)
sp = np.asarray(Image.fromarray((sp*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))).astype(np.float32)/255
lum = lum + sp * 55
pan = np.clip(target[None, None, :] + lum[..., None] * np.array([1.0, 0.9, 0.88]), 0, 255)
# máscara com borda suave, 2px para dentro do aro
m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).rounded_rectangle((2, 2, W-3, H-3), radius=6, fill=255)
m = np.asarray(m.filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32)[..., None]/255
region = A[BR[1]:BR[3], BR[0]:BR[2]]
A[BR[1]:BR[3], BR[0]:BR[2]] = region*(1-m) + pan*m
res = Image.fromarray(np.clip(A, 0, 255).astype(np.uint8)); res.save(out)
res.crop((480, 480, 880, 720)).resize((1200, 720), Image.LANCZOS).save(prev)
print('ok', np.asarray(res.crop(BR).convert('L')).std())
