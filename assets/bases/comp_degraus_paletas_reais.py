import sys, numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
S="/tmp/claude-0/-home-user-LFPRO-STUDIO-IMAGES/e2f30a37-5666-53de-90d4-f3cfc5463931/scratchpad"
scene=Image.open(f"{S}/dl2/empty.png").convert("RGBA")
W,H=scene.size
def cutout(n):
    src=Image.open(f"{S}/drive3/{n}.png").convert("RGB"); im=np.asarray(src).astype(float)
    dist=np.sqrt(((im-np.array([249.,247.,244.]))**2).sum(-1))
    c=Image.fromarray(np.where(dist<95,255,0).astype(np.uint8)).copy(); ImageDraw.floodfill(c,(0,0),128)
    fg=Image.fromarray(np.where(np.asarray(c)==128,0,255).astype(np.uint8)).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(0.7))
    o=src.convert("RGBA"); o.putalpha(fg); return o
def H_(src,dst):  # homography mapping dst->src for PIL
    A=[];b=[]
    for (x,y),(X,Y) in zip(dst,src):
        A.append([x,y,1,0,0,0,-X*x,-X*y]); b.append(X)
        A.append([0,0,0,x,y,1,-Y*x,-Y*y]); b.append(Y)
    return np.linalg.solve(np.array(A,float),np.array(b,float))
def warp(img,src,dst):
    w=img.transform((W,H),Image.PERSPECTIVE,tuple(H_(src,dst)),Image.BICUBIC)
    m=Image.new("L",(W,H),0); ImageDraw.Draw(m).polygon([tuple(p) for p in dst],fill=255)
    a=Image.fromarray(np.minimum(np.asarray(w.getchannel("A")),np.asarray(m.filter(ImageFilter.GaussianBlur(0.6))))); w.putalpha(a); return w
plinths={ # F, R, L, B
 1:((355,1965),(722,1780),(80,1665),(435,1487)),
 2:((735,1670),(1085,1490),(438,1380),(778,1207)),
 3:((1105,1370),(1440,1200),(798,1102),(1112,942)),
 4:((1460,1090),(1788,925),(1143,833),(1455,680)),
}
order={1:"sunset",2:"basic",3:"petal",4:"stone"}
offs={"sunset":(4,4),"basic":(2,3),"petal":(0,0),"stone":(9,5)}
U0,U1,V0,V1=0.13,0.87,0.14,0.70
LIDH=float(sys.argv[1]) if len(sys.argv)>1 else 0.95
TILT=float(sys.argv[2]) if len(sys.argv)>2 else 0.10
DARK=0.9
for k in (1,2,3,4):
    F,R,L,B=[np.array(p,float) for p in plinths[k]]
    P=lambda u,v: F+u*(R-F)+v*(L-F)+u*v*(B-R-L+F)
    n=order[k]; dx,dy=offs[n]; img=cutout(n)
    img=ImageEnhance.Brightness(img).enhance(DARK)
    tf0,tf1,tb1,tb0=P(U0,V0),P(U1,V0),P(U1,V1),P(U0,V1)
    tray_src=[(460+dx,747+dy),(872+dx,747+dy),(865+dx,505+dy),(467+dx,505+dy)]
    tray_dst=[tf0,tf1,tb1,tb0]
    depth_px=np.linalg.norm(tb0-tf0); up=np.array([0,-1.0])*depth_px*LIDH + (L-F)/np.linalg.norm(L-F)*depth_px*TILT
    lid_dst=[tb0,tb1,tb1+up,tb0+up]
    lid_src=[(468+dx,492+dy),(864+dx,492+dy),(877+dx,312+dy),(455+dx,312+dy)]
    # shadows: contact under tray + lid cast toward lower-right
    sh=Image.new("L",(W,H),0); d=ImageDraw.Draw(sh)
    off=np.array([14,12]); d.polygon([tuple(p+off) for p in tray_dst],fill=200)
    lidfoot=[tb0,tb1,tb1+(R-F)/np.linalg.norm(R-F)*20+np.array([10,25]),tb0+np.array([10,25])]
    d.polygon([tuple(p) for p in lidfoot],fill=160)
    sh=sh.filter(ImageFilter.GaussianBlur(16)); shadow=Image.new("RGBA",(W,H),(0,0,0,0)); shadow.putalpha(sh.point(lambda v:int(v*0.75)))
    scene.alpha_composite(shadow)
    scene.alpha_composite(warp(img,lid_src,lid_dst))
    scene.alpha_composite(warp(img,tray_src,tray_dst))
out=scene.convert("RGB"); out.save("comp.png"); out.resize((W//2,H//2)).save("comp-half.jpg",quality=90)
for i,(x0,y0,x1,y1) in enumerate([(0,1350,800,2050),(1000,550,1856,1250)]): out.crop((x0,y0,x1,y1)).save(f"zoom{i}.jpg",quality=92)
print("ok")
