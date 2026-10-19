import sys, json
import numpy as np
from PIL import Image, ImageFilter, ImageChops, ImageEnhance
# uso: compose.py cut.png out.png '[{"x":540,"y":900,"scale":1.3,"rot":-8,"dim":1.0,"refl":true},...]' [W H]
# cada camada aceita "cut":"outro.png" para misturar produtos (ex.: PETAL + BASIC)
cut, out, layers = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
W, H = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (1080, 1920)
P0 = Image.open(cut).convert('RGBA')
canvas = Image.new('RGB', (W, H), (0, 0, 0))
# leve gradiente de estúdio (preto puro nas bordas, quase preto no centro)
yy, xx = np.mgrid[0:H, 0:W]
g = np.clip(1 - np.sqrt(((xx-W/2)/(W*0.75))**2 + ((yy-H*0.45)/(H*0.6))**2), 0, 1) * 14
canvas = Image.fromarray(np.dstack([g*1.0, g*0.9, g*0.8]).astype(np.uint8))
def place(L):
    P = Image.open(L['cut']).convert('RGBA') if 'cut' in L else P0
    p = P.resize((int(P.width*L['scale']), int(P.height*L['scale'])), Image.LANCZOS)
    if L.get('dim', 1) != 1:
        rgb = ImageEnhance.Brightness(p.convert('RGB')).enhance(L['dim']); rgb.putalpha(p.getchannel('A')); p = rgb
    p = p.rotate(L['rot'], resample=Image.BICUBIC, expand=True)
    a = p.getchannel('A')
    ox, oy = int(L['x'] - p.width/2), int(L['y'] - p.height/2)
    # sombra de contato
    sh = Image.new('L', (W, H), 0); sh.paste(a, (ox+10, oy+26)); sh = sh.filter(ImageFilter.GaussianBlur(28))
    base = canvas.convert('RGB'); canvas_sh = Image.composite(Image.new('RGB', (W, H), (0,0,0)), base, sh.point(lambda v: int(v*0.85)))
    # reflexo na superfície
    if L.get('refl'):
        r = p.transpose(Image.FLIP_TOP_BOTTOM)
        ra = r.getchannel('A'); grad = Image.linear_gradient('L').resize(r.size).point(lambda v: int(max(0, 255-v*2.2)*0.22))
        ra = ImageChops.multiply(ra, grad); r.putalpha(ra); r = r.filter(ImageFilter.GaussianBlur(2))
        canvas_sh.paste(r, (ox, oy + p.height - 6), r)
    # contorno quente (rim light) a partir da borda do alfa
    edge = ImageChops.subtract(a, a.filter(ImageFilter.MinFilter(3))).filter(ImageFilter.GaussianBlur(1.5))
    rim = Image.new('RGBA', p.size, (214, 170, 110, 0)); rim.putalpha(edge.point(lambda v: int(v*0.22*L.get('dim',1))))
    canvas_sh.paste(p, (ox, oy), p); canvas_sh.paste(rim, (ox, oy), rim)
    return canvas_sh
for L in layers: canvas = place(L)
canvas.save(out); print('ok', out, canvas.size)
