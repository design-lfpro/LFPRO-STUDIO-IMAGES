import sys
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB'); A = np.asarray(im).astype(np.float32)
bg = np.median(np.concatenate([A[:20].reshape(-1,3), A[-20:].reshape(-1,3)]), axis=0)
d = np.sqrt(((A - bg)**2).sum(-1))
m = Image.fromarray(((d > 60)*255).astype(np.uint8))
m = m.filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.MinFilter(7))   # closing
# preencher buracos: flood fill do fundo a partir da borda
f = m.copy(); ImageDraw.floodfill(f, (0, 0), 128)
F = np.asarray(f); M = np.where(F == 128, 0, 255).astype(np.uint8)
m = Image.fromarray(M).filter(ImageFilter.MinFilter(9))                    # erode 4px (remove halo)
alpha = m.filter(ImageFilter.GaussianBlur(0.8))
# descontaminar borda: pixels claros na faixa da borda viram preto do estojo
Am = np.asarray(alpha).astype(np.float32)/255; R = A.copy()
band = (Am > 0) & (Am < 0.999)
lum = R.mean(-1); fix = band & (lum > 60)
R[fix] = R[fix] * 0.15
rgba = Image.fromarray(R.astype(np.uint8)); rgba.putalpha(alpha)
bb = alpha.getbbox(); rgba.crop(bb).save(out)
print(src.split('/')[-2], 'bg', bg.astype(int), 'bbox', bb)
