from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import numpy as np
c=Image.open('cut04.png').convert('RGBA')
c=c.crop(c.getchannel('A').point(lambda a:255 if a>20 else 0).getbbox())
rgb=c.convert('RGB'); a=c.getchannel('A')
rgb=Image.blend(rgb, ImageEnhance.Color(rgb).enhance(0.0), 0.35)
rgb=Image.fromarray((255*(np.asarray(rgb)/255.0)**0.72*1.15).clip(0,255).astype('uint8'))
c=Image.merge('RGBA',(*rgb.split(),a))
c=c.rotate(-13, resample=Image.BICUBIC, expand=True)   # tilt clockwise like the montage
c=c.crop(c.getbbox())
W,H=1500,2000
sw,sh=c.size; s=1560/sh; c=c.resize((int(sw*s),int(sh*s)),Image.LANCZOS); sw,sh=c.size
x=(W-sw)//2+20; y=int(H*0.07)
floor=int(H*0.93)
yy,xx=np.mgrid[0:H,0:W]
d=np.sqrt(((xx-W/2)/(W*0.6))**2+((yy-H*0.45)/(H*0.55))**2)
d2=np.sqrt(((xx-W*0.6)/(W*0.45))**2+((yy-H*0.35)/(H*0.45))**2)
g=np.clip(1-d2,0,1)**1.6
bg=np.zeros((H,W,3)); bg[...,0]=4+40*g; bg[...,1]=3+30*g; bg[...,2]=3+17*g
# textured floor at bottom (fine grain), fading up
rng=np.random.default_rng(1); grain=rng.normal(0,1,(H,W))
grain=np.array(Image.fromarray(((grain*30)+128).clip(0,255).astype('uint8')).filter(ImageFilter.GaussianBlur(0.8))).astype(float)-128
fl=np.clip((yy-H*0.84)/(H*0.16),0,1)*np.clip(1-abs(xx-W/2)/(W*0.75),0,1)
for i,k in enumerate((20,16,12)): bg[...,i]+=fl*(k+grain*0.35)
img=Image.fromarray(bg.clip(0,255).astype('uint8')).convert('RGBA')
# soft floor shadow under floating sponge
sm=Image.new('L',(W,H),0); cx=x+sw*0.45
ImageDraw.Draw(sm).ellipse((cx-sw*0.35,floor-20,cx+sw*0.35,floor+25),fill=200)
sm=sm.filter(ImageFilter.GaussianBlur(30)); blk=Image.new('RGBA',(W,H),(0,0,0,0)); blk.putalpha(sm); img.alpha_composite(blk)
lay=Image.new('RGBA',(W,H),(0,0,0,0)); lay.paste(c,(x,y)); img.alpha_composite(lay)
v=np.clip(1-0.5*np.clip(d-0.35,0,1),0,1)
out=(np.array(img.convert('RGB')).astype(float)*v[...,None]).clip(0,255).astype('uint8')
Image.fromarray(out).save('hero_float_3x4.png'); Image.fromarray(out).resize((600,800)).save('hero_float_prev.jpg')
