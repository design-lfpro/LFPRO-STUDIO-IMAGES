---
family: lapis-labios
title: Lápis para Lábios
product_type: Lápis para Lábios
status: dna-v1
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
handles:
  - lapis-labios-caramelo
  - lapis-labios-chocolate
  - lapis-labios-magenta
---

# Lápis para Lábios — DNA de família

Lápis gel labial preto slim. Tons: Caramelo, Chocolate, Magenta. Também aparece nos Lip Combos.

## Packaging (lock visual)

| Elemento | Lock |
|----------|------|
| **Corpo** | Preto matte slim |
| **Texto** | Vertical gold: `LÁPIS PARA LÁBIOS` + monograma LF gold |
| **Color tip** | Extremidade inferior na cor do tom |
| **Cap** | Preto curto ao lado (packshot solo) |
| **Ponta** | Afiação cônica na cor |

**Diferença vs lápis olhos:** texto **LÁBIOS** (não OLHOS); nos combos o lápis costuma aparecer **horizontal** com texto horizontal.

## Claims família

- Fórmula gel: textura macia cremosa
- Pigmentação intensa; longa duração; resistência à água; sem borrar
- Contornar, preencher ou esfumar
- Não resseca, não craquela
- Apontar só com apontador de maquiagem lâmina fina

## Prompt anchors (EN)

```
LF PRO lip pencil identity lock: matte black pencil, gold text "LÁPIS PARA LÁBIOS", gold LF monogram, color tip matching shade, sharpened tip, black cap beside. Off-white background. Photorealistic.
```

## Anti-patterns

- Não confundir com lápis de olhos
- Não omitir color tip
- Não inventar tons além de Caramelo/Chocolate/Magenta
- **Não perder acentos no texto** — falha observada (2026-09-08): "LAPIS PARA LABIOS" sem acento; correto é sempre **LÁPIS PARA LÁBIOS**
- **Não inventar frisos/anéis dourados no corpo** — falha observada; o corpo é liso, só tem o texto vertical + monograma, nada de hardware metálico extra
- **Cone apontado é PRETO, não madeira clara** — falha observada (2026-09-28): IA desenhou cone de madeira bege natural; o real é cone preto fosco com a ponta da mina na cor do tom
- **Proporção:** lápis muito longo e fino (~20× o diâmetro); a faixa de cor da extremidade traseira ocupa ~8% do comprimento, corte reto
- **Cap:** curto e mais largo que o corpo (ver packshot solo 01); em composições horizontais preferir **sem cap** — a IA tende a inventar um cap longo e fino
- **Referência horizontal oficial:** `assets/products/lip-combo-nude-essencial/01.png` (lápis Caramelo deitado + Classic Lips Amber) — usar como ref principal quando o lápis aparecer na horizontal ou em composição com batom

## Notas V1

- Solo: layout vertical 01
- Em combos: layout horizontal — reutilizar DNA
