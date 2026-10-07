import base64, io, sys
from PIL import Image
ROOT = sys.argv[1]; OUT = sys.argv[2]

def b64(handle, size=520):
    im = Image.open(f"{ROOT}/assets/products/{handle}/01.png").convert("RGB")
    im.thumbnail((size, size))
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=88)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

products = [
    ("po-soft-eye-claro", "PÓ SOFT EYE", "Pó solto · área dos olhos", "109,90"),
    ("base-soft-matte-cor-05", "BASE SOFT MATTE", "Base líquida · 30ml", "109,90"),
    ("cream-color-candy-blush-e-iluminador", "CREAM COLOR", "Blush e iluminador", "99,90"),
]

W, H = 1080, 1920
card_x, card_w, card_h, gap = 72, 936, 300, 24
y0 = 520

cards = []
for i, (h, name, sub, de) in enumerate(products):
    y = y0 + i * (card_h + gap)
    n = i + 1
    cards.append(f'''
  <g id="produto-{n}">
    <rect x="{card_x}" y="{y}" width="{card_w}" height="{card_h}" rx="28" fill="#141414" stroke="#C9A45C" stroke-opacity="0.35" stroke-width="2"/>
    <rect x="{card_x+16}" y="{y+16}" width="{card_h-32}" height="{card_h-32}" rx="20" fill="#F7F5F2"/>
    <image id="produto-{n}-foto" x="{card_x+16}" y="{y+16}" width="{card_h-32}" height="{card_h-32}" preserveAspectRatio="xMidYMid meet" href="{b64(h)}"/>
    <text id="produto-{n}-nome" x="{card_x+card_h+20}" y="{y+72}" class="nome">{name}</text>
    <text id="produto-{n}-sub" x="{card_x+card_h+20}" y="{y+110}" class="sub">{sub}</text>
    <text x="{card_x+card_h+20}" y="{y+170}" class="de">DE: <tspan id="produto-{n}-de" class="de-valor">R$ {de}</tspan></text>
    <line id="produto-{n}-risco" x1="{card_x+card_h+80}" y1="{y+160}" x2="{card_x+card_h+80+int(len("R$ "+de)*16.6)}" y2="{y+160}" stroke="#E63E3E" stroke-width="4"/>
    <text x="{card_x+card_h+20}" y="{y+250}" class="por">POR: <tspan id="produto-{n}-por" class="por-valor">R$ 00,00</tspan></text>
  </g>''')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <!-- LF PRO · Story patrocinado · Black November · 1080x1920
       Zonas seguras Instagram Ads: topo 0-250 (perfil/patrocinado) e base 1580-1920 (CTA) sem conteúdo crítico.
       Editar: textos #produto-N-de / #produto-N-por, #data-live; trocar fotos em #produto-N-foto (packshot do site). -->
  <defs>
    <style>
      text {{ font-family: Montserrat, 'Helvetica Neue', Arial, sans-serif; }}
      .nome {{ font-size: 40px; font-weight: 700; fill: #FFFFFF; letter-spacing: 3px; }}
      .sub {{ font-size: 26px; font-weight: 400; fill: #B8B2A7; }}
      .de {{ font-size: 30px; font-weight: 500; fill: #8E8A84; letter-spacing: 1px; }}
      .de-valor {{ fill: #8E8A84; }}
      .por {{ font-size: 34px; font-weight: 600; fill: #C9A45C; letter-spacing: 1px; }}
      .por-valor {{ font-size: 64px; font-weight: 800; fill: #E2C27A; letter-spacing: 0; }}
    </style>
    <radialGradient id="glow" cx="50%" cy="38%" r="60%">
      <stop offset="0" stop-color="#2A2116"/>
      <stop offset="1" stop-color="#050505"/>
    </radialGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#B8883E"/><stop offset="0.5" stop-color="#F1D38A"/><stop offset="1" stop-color="#B8883E"/>
    </linearGradient>
  </defs>

  <rect id="fundo" width="{W}" height="{H}" fill="url(#glow)"/>

  <!-- zona segura topo (guia, não imprime conteúdo) -->
  <g id="guia-safe-zones" opacity="0" pointer-events="none">
    <rect x="0" y="0" width="{W}" height="250" fill="#ff00ff"/>
    <rect x="0" y="1580" width="{W}" height="340" fill="#ff00ff"/>
  </g>

  <!-- faixa Black November -->
  <g id="faixa">
    <rect x="72" y="270" width="936" height="76" fill="#E63E3E"/>
    <text x="540" y="321" text-anchor="middle" font-size="31" font-weight="700" fill="#FFFFFF" letter-spacing="9">BLACK NOVEMBER • LIVE • LF PRO</text>
  </g>

  <!-- headline -->
  <g id="headline">
    <text x="540" y="418" text-anchor="middle" font-size="58" font-weight="800" fill="#FFFFFF" letter-spacing="2">PREÇO DE LIVE</text>
    <text x="540" y="472" text-anchor="middle" font-size="30" font-weight="400" fill="#C9A45C" letter-spacing="6">NOS QUERIDINHOS DA LF PRO</text>
  </g>
{''.join(cards)}

  <!-- data / chamada -->
  <g id="rodape">
    <line x1="340" y1="1500" x2="740" y2="1500" stroke="url(#gold)" stroke-width="2"/>
    <text id="data-live" x="540" y="1552" text-anchor="middle" font-size="36" font-weight="700" fill="#FFFFFF" letter-spacing="4">AO VIVO · 00/11 ÀS 20H</text>
  </g>
</svg>
'''
open(OUT, "w").write(svg)
print(len(svg)//1024, "KB")
