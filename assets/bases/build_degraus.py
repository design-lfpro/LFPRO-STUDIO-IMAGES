import numpy as np
from PIL import Image, ImageDraw, ImageFilter
D="/tmp/claude-0/-home-user-LFPRO-STUDIO-IMAGES/e2f30a37-5666-53de-90d4-f3cfc5463931/scratchpad/drive3"
def cut(n):
    src=Image.open(f"{D}/{n}.png").convert("RGB"); im=np.asarray(src).astype(float)
    dist=np.sqrt(((im-np.array([249.,247.,244.]))**2).sum(-1))
    c=Image.fromarray(np.where(dist<95,255,0).astype(np.uint8)).copy(); ImageDraw.floodfill(c,(0,0),128)
    fg=Image.fromarray(np.where(np.asarray(c)==128,0,255).astype(np.uint8)).filter(ImageFilter.MinFilter(9)).filter(ImageFilter.GaussianBlur(0.8))
    rgba=src.convert("RGBA"); rgba.putalpha(fg)
    bb=fg.point(lambda v:255 if v>128 else 0).getbbox(); rgba=rgba.crop(bb)
    x0=int(rgba.width*0.395); o=rgba.crop((x0,0,rgba.width,rgba.height)); return o.crop(o.getchannel("A").getbbox())
W,H=1080,1350
# background: charcoal wall + floor
y=np.linspace(0,1,H)[:,None]; x=np.linspace(0,1,W)[None,:]
wall=14+16*np.exp(-((x-0.25)**2/0.18+(y-0.3)**2/0.25))
img=np.repeat(wall[...,None],3,2)*np.array([1,0.97,0.94])
floor_y=1180
img[floor_y:]=np.repeat((26+10*np.exp(-((x-0.3)**2/0.2)))[...,None],3,2)[0]*np.array([1,.97,.94])
canvas=Image.fromarray(img.clip(0,255).astype(np.uint8)).convert("RGBA")
d=ImageDraw.Draw(canvas)
names=["sunset","basic","petal","stone"]; tops=[1010,880,750,620]; pw=250; x0=40; depth=34
for i,(n,t) in enumerate(zip(names,tops)):
    X=x0+i*pw
    # floor shadow
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rectangle((X+20,floor_y-6,X+pw+40,floor_y+40),fill=(0,0,0,150)); canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
    # front face gradient
    g=np.linspace(58,24,floor_y-t)[:,None]*np.ones((1,pw)); g=g*(1-0.18*np.linspace(0,1,pw))[None,:]
    canvas.alpha_composite(Image.fromarray(np.dstack([g,g*0.98,g*0.96,np.full_like(g,255)]).astype(np.uint8),"RGBA"),(X,t))
    # top face (parallelogram)
    d.polygon([(X,t),(X+pw,t),(X+pw+depth*0.6,t-depth),(X+depth*0.6,t-depth)],fill=(78,75,72,255))
    d.line([(X,t),(X+pw,t)],fill=(110,105,100,255),width=2); d.line([(X,t),(X,floor_y)],fill=(80,76,72,255),width=2)
for i,(n,t) in enumerate(zip(names,tops)):
    X=x0+i*pw; p=cut(n); s=(pw-28)/p.width; p=p.resize((int(p.width*s),int(p.height*s)),Image.LANCZOS)
    px=X+14+int(depth*0.3); py=t-int(depth*0.45)-p.height
    a=p.getchannel("A"); sh=Image.new("RGBA",p.size,(0,0,0,0)); sh.putalpha(a.point(lambda v:int(v*.75)))
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)),(px+10,py+12))
    canvas.alpha_composite(p,(px,py))
canvas.convert("RGB").save("base-degraus.png"); print("ok")
