"""Story patrocinado Black November — produto único (DE/POR).
Uso: python3 build_story_single.py <repo_root> <out.svg> <handle> "<NOME>" "<subtítulo>" "<preço DE>"
"""
import base64, io, sys
from PIL import Image

ROOT, OUT, HANDLE, NAME, SUB, DE = sys.argv[1:7]

im = Image.open(f"{ROOT}/assets/products/{HANDLE}/01.png").convert("RGB")
im.thumbnail((1000, 1000))
buf = io.BytesIO(); im.save(buf, "JPEG", quality=90)
foto = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

W, H = 1080, 1920
de_txt = f"R$ {DE}"
risco_x1 = 540 - (len("DE: " + de_txt) * 21) // 2 + 4 * 21
risco_x2 = risco_x1 + len(de_txt) * 21 - 10

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <!-- LF PRO · Story patrocinado · Black November · PRODUTO ÚNICO · 1080x1920
       Zonas seguras Instagram Ads: topo 0-250 (perfil/patrocinado) e base 1580-1920 (CTA) sem conteúdo crítico.
       Editar: #produto-nome, #produto-sub, #produto-de, #produto-por, #data-live; trocar foto em #produto-foto (packshot do site). -->
  <defs>
    <style>text {{ font-family: Montserrat, 'Helvetica Neue', Arial, sans-serif; }}</style>
    <radialGradient id="glow" cx="50%" cy="44%" r="58%">
      <stop offset="0" stop-color="#2E2418"/>
      <stop offset="1" stop-color="#050505"/>
    </radialGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#B8883E"/><stop offset="0.5" stop-color="#F1D38A"/><stop offset="1" stop-color="#B8883E"/>
    </linearGradient>
    <clipPath id="foto-clip"><rect x="160" y="490" width="760" height="680" rx="36"/></clipPath>
  </defs>

  <rect id="fundo" width="{W}" height="{H}" fill="url(#glow)"/>

  <g id="guia-safe-zones" opacity="0" pointer-events="none">
    <rect x="0" y="0" width="{W}" height="250" fill="#ff00ff"/>
    <rect x="0" y="1580" width="{W}" height="340" fill="#ff00ff"/>
  </g>

  <g id="faixa">
    <rect x="72" y="270" width="936" height="76" fill="#E63E3E"/>
    <text x="540" y="321" text-anchor="middle" font-size="31" font-weight="700" fill="#FFFFFF" letter-spacing="9">BLACK NOVEMBER • LIVE • LF PRO</text>
  </g>

  <g id="headline">
    <text x="540" y="414" text-anchor="middle" font-size="52" font-weight="800" fill="#FFFFFF" letter-spacing="2">PREÇO DE LIVE</text>
    <text id="data-live" x="540" y="462" text-anchor="middle" font-size="28" font-weight="500" fill="#C9A45C" letter-spacing="6">AO VIVO · 00/11 ÀS 20H</text>
  </g>

  <g id="produto">
    <rect x="152" y="482" width="776" height="696" rx="42" fill="none" stroke="url(#gold)" stroke-width="2" stroke-opacity="0.7"/>
    <rect x="160" y="490" width="760" height="680" rx="36" fill="#F7F5F2"/>
    <image id="produto-foto" x="160" y="490" width="760" height="680" preserveAspectRatio="xMidYMid slice" clip-path="url(#foto-clip)" href="{foto}"/>
    <text id="produto-nome" x="540" y="1252" text-anchor="middle" font-size="58" font-weight="700" fill="#FFFFFF" letter-spacing="5">{NAME}</text>
    <text id="produto-sub" x="540" y="1300" text-anchor="middle" font-size="30" font-weight="400" fill="#B8B2A7">{SUB}</text>
  </g>

  <g id="preco">
    <text x="540" y="1384" text-anchor="middle" font-size="38" font-weight="500" fill="#8E8A84" letter-spacing="1">DE: <tspan id="produto-de">{de_txt}</tspan></text>
    <line id="produto-risco" x1="{risco_x1}" y1="1371" x2="{risco_x2}" y2="1371" stroke="#E63E3E" stroke-width="5"/>
    <text x="540" y="1515" text-anchor="middle" fill="#C9A45C"><tspan font-size="42" font-weight="600" letter-spacing="1">POR: </tspan><tspan id="produto-por" font-size="112" font-weight="800" fill="#E2C27A">R$ 00,00</tspan></text>
  </g>
</svg>
'''
open(OUT, "w").write(svg)
print(OUT, len(svg) // 1024, "KB")
