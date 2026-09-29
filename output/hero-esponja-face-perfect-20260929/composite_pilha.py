from PIL import Image, ImageFilter, ImageEnhance
import numpy as np, random
random.seed(7); np.random.seed(7)
W,H=1800,2400
def prep(n):
    c=Image.open(n).convert('RGBA'); a=c.getchannel('A')
    rgb=np.asarray(c.convert('RGB')).astype(float)
    m=np.asarray(a)>128
    # neutralize color cast, normalize luminance of the sponge
    lum=rgb.mean(axis=2,keepdims=True)
    rgb=0.15*rgb+0.85*lum
    mean=rgb[m].mean(); rgb=rgb*(30/mean)
    return Image.merge('RGBA',(*Image.fromarray(rgb.clip(0,255).astype('uint8')).split(),a))
src=[prep(n) for n in ['cut01.png','cut03L.png','cut03M.png','cut04.png']]
weights=[3,2,2,2]
canvas=Image.new('RGBA',(W,H),(6,6,6,255))
layers=[  # (count, height px range, blur, brightness)
 (120,(360,480),2.0,0.55),
 (100,(400,520),0.8,0.75),
 (75,(430,560),0.0,0.95),
 (45,(460,600),0.0,1.1),
]
for count,(h0,h1),blur,br in layers:
    # jittered grid so the surface is fully covered
    cols=int(np.ceil(np.sqrt(count*W/H))); rows=int(np.ceil(count/cols))
    cells=[(i,j) for i in range(cols) for j in range(rows)]; random.shuffle(cells)
    for i,j in cells[:count]:
        c=random.choices(src,weights)[0]
        h=random.uniform(h0,h1); s=h/c.height
        sp=c.resize((max(1,int(c.width*s)),int(h)),Image.LANCZOS)
        sp=sp.rotate(random.uniform(0,360),resample=Image.BICUBIC,expand=True)
        rgb=ImageEnhance.Brightness(sp.convert('RGB')).enhance(br*random.uniform(0.85,1.15))
        sp=Image.merge('RGBA',(*rgb.split(),sp.getchannel('A')))
        if blur: sp=sp.filter(ImageFilter.GaussianBlur(blur))
        cx=(i+random.uniform(0.1,0.9))*W/cols; cy=(j+random.uniform(0.1,0.9))*H/rows
        x=int(cx-sp.width/2); y=int(cy-sp.height/2)
        # contact/ambient shadow onto what is underneath
        sh=sp.getchannel('A').filter(ImageFilter.GaussianBlur(20)).point(lambda v:int(v*0.85))
        shl=Image.new('RGBA',sp.size,(0,0,0,0)); shl.putalpha(sh)
        canvas.alpha_composite(shl,(max(0,x+10),max(0,y+18))) if x+10>=0 and y+18>=0 else None
        tmp=Image.new('RGBA',(W,H),(0,0,0,0)); tmp.paste(shl,(x+10,y+18),shl); canvas.alpha_composite(tmp)
        tmp=Image.new('RGBA',(W,H),(0,0,0,0)); tmp.paste(sp,(x,y),sp); canvas.alpha_composite(tmp)
img=np.asarray(canvas.convert('RGB')).astype(float)
yy,xx=np.mgrid[0:H,0:W]
# unify light: soft key from upper-left + gentle warm tone + vignette
key=0.75+0.45*np.clip(1-np.sqrt(((xx-W*0.3)/W)**2+((yy-H*0.25)/H)**2)*1.3,0,1)
vig=np.clip(1-0.45*np.clip(np.sqrt(((xx-W/2)/(W*0.7))**2+((yy-H/2)/(H*0.7))**2)-0.4,0,1),0,1)
img=img*(key*vig)[...,None]; img[...,0]*=1.03; img[...,2]*=0.97
out=Image.fromarray(img.clip(0,255).astype('uint8'))
out.save('pile2_3x4.png'); out.resize((600,800)).save('pile2_prev.jpg')
