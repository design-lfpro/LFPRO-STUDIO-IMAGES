import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageChops, ImageEnhance
D="/tmp/claude-0/-home-user-LFPRO-STUDIO-IMAGES/e2f30a37-5666-53de-90d4-f3cfc5463931/scratchpad/drive3"
scene=Image.open('scene.png').convert('RGBA'); W,H=scene.size
def cut(n):
    src=Image.open(f"{D}/{n}.png").convert("RGB"); im=np.asarray(src).astype(float)
    dist=np.sqrt(((im-np.array([249.,247.,244.]))**2).sum(-1))
    c=Image.fromarray(np.where(dist<95,255,0).astype(np.uint8)).copy(); ImageDraw.floodfill(c,(0,0),128)
    fg=Image.fromarray(np.where(np.asarray(c)==128,0,255).astype(np.uint8)).filter(ImageFilter.MinFilter(11)).filter(ImageFilter.GaussianBlur(0.9))
    o=src.convert("RGBA"); o.putalpha(fg)
    o=o.crop((456,0,1080,1080)); return o.crop(o.getchannel('A').getbbox())
def grade(p):
    a=p.getchannel('A'); rgb=np.asarray(p.convert('RGB')).astype(float)
    rgb=rgb*np.array([1.0,0.96,0.9])*0.9
    o=Image.fromarray(rgb.clip(0,255).astype(np.uint8)).convert('RGBA'); o.putalpha(a); return o
layout=[ # name, width, center x, bottom y, rotation
 ('basic',420,262,1625,-4),
 ('stone',420,1594,1625,4),
 ('petal',480,698,1712,-1.5),
 ('sunset',480,1158,1712,1.5),
]
for n,w,cx,by,rot in layout:
    p=grade(cut(n)); s=w/p.width; p=p.resize((w,int(p.height*s)),Image.LANCZOS)
    p=p.rotate(rot,resample=Image.BICUBIC,expand=True)
    x=int(cx-p.width/2); y=int(by-p.height)
    # reflection
    r=ImageOps.flip(p); grad=Image.linear_gradient('L').resize(r.size).point(lambda v:int(max(0,255-v*3.2)*0.32))
    r.putalpha(ImageChops.multiply(r.getchannel('A'),grad)); r=r.filter(ImageFilter.GaussianBlur(1.5))
    scene.alpha_composite(r,(x,by+2))
    # contact shadow
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).ellipse((cx-w*0.48,by-14,cx+w*0.48,by+16),fill=(0,0,0,200))
    scene.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)))
    scene.alpha_composite(p,(x,y))
out=scene.convert('RGB'); out.save('pir.png'); out.resize((W*2//5,H*2//5)).save('pir-s.jpg',quality=90)
