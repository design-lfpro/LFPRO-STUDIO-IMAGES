---
family: kit-cream-color
title: Kit Cream Color + Pincel B03
product_type: Kit
handles:
  - kit-cream-color-candy-e-pincel-b03
  - kit-cream-color-merlot-pincel-b03
  - kit-cream-color-rose-e-pincel-b03
  - kit-cream-color-cocoa-pincel-b03
  - kit-cream-color-toffee-pincel-b03
  - ki-cream-color-taupe-e-pincel-b03
  - paleta-cream-color-cor-peach-pincel-b03
status: dna-v1
preferred_tracks: [T1-product-hero, T2-texture-macro, T3-tools-hands]
blocked_tracks: [T5-face-proof]
components:
  palette_family: cream-color
  brush_handle: pincel-duplo-blush-e-iluminador-b03
updated: 2026-08-06
---

# Kit Cream Color + Pincel B03 — DNA da família

**Kits de e-commerce** que unem **1 paleta Cream Color** + **1 Pincel duplo B03**. Preço kit site: **R$ 179,80**. Cada kit herda o DNA visual da paleta correspondente e o packaging do B03.

> **Gotcha de handles Shopify:**  
> - Taupe: `ki-cream-color-taupe-e-pincel-b03` (typo **ki-** sem t)  
> - Peach: `paleta-cream-color-cor-peach-pincel-b03` (prefixo paleta-, não kit-)

## Componentes (sempre linkar)

| Componente | Handle / família | Lock |
|------------|------------------|------|
| Paleta | família [[../cream-color/_family|cream-color]] | compacto preto+ouro, 2 panos |
| Pincel B03 | `pincel-duplo-blush-e-iluminador-b03` | cabo preto double-ended, cerdas sintéticas dual, monograma LF + **LF PRO** vertical + **B03** em gold |

## Pincel B03 — lock visual

1. **Cabo** — plástico preto brilhante, forma **dupla** (dois ferules opostos), cintura central mais fina.
2. **Cerdas** — sintéticas **preto → branco** (two-tone), uma ponta **maior/cheia** (blush), outra **menor/precisa** (iluminador).
3. **Marca no cabo** — monograma **LF** gold + barra + wordmark vertical **LF PRO** + código **B03** em ouro.
4. **Duplo polimento** (claim): acabamento sem marcas, distribuição uniforme.

## Gramática fotográfica do kit

| Tipo | Composição | Fundo |
|------|------------|-------|
| **01 Hero kit** | Paleta aberta + B03 inclinado/apoiado | Off-white #FAFAF8 |
| Beauty | Modelo + paleta e/ou B03 | Âmbar campaign |

## Claims do kit (site — sem inventar)

- Blush, glow e acabamento impecável em cada aplicação
- Combinação paleta + B03: aplicação precisa, distribuição uniforme, camadas sem esforço
- Fórmula cremosa multifuncional se funde à pele
- Cerdas sintéticas de duplo polimento; design para blush e iluminador
- Acabamento mais natural e refinado; glow mais uniforme; blush perfeitamente esfumado
- Performance com praticidade

## Prompt anchors da família (EN)

### Packaging + brush lock

```
LF PRO Cream Color kit: open high-gloss black dual cream compact with gold dual pans and gold LF PRO monogram closed compact optional, plus LF PRO B03 dual-ended makeup brush black glossy handle with gold monogram LF / LF PRO and B03 lettering, two-tone black-to-white synthetic dual brush heads (larger fluffy end and smaller precise end), luxury Brazilian cosmetics still life on off-white seamless
```

### Anti-patterns

- Inventar pincel de cabo dourado ou cerdas coloridas
- Omitir código B03 ou monograma
- Paleta com cores do shade errado
- Tratar kit como produto único sem herança dos componentes
- Face-proof inventado

## Mapa kit → componentes

| Kit handle | Paleta | Shade |
|------------|--------|-------|
| kit-cream-color-candy-e-pincel-b03 | cream-color-candy-blush-e-iluminador | Candy |
| kit-cream-color-merlot-pincel-b03 | cream-color-merlot-blush-e-iluminador | Merlot |
| paleta-cream-color-cor-peach-pincel-b03 | cream-color-peach-blush-e-iluminador | Peach |
| kit-cream-color-rose-e-pincel-b03 | paleta-cream-color-blush-e-iluminador-cor-rose | Rose |
| ki-cream-color-taupe-e-pincel-b03 | paleta-cream-color-blush-e-iluminador-cor-taupe | Taupe |
| kit-cream-color-cocoa-pincel-b03 | cream-color-contorno-cocoa | Cocoa |
| kit-cream-color-toffee-pincel-b03 | paleta-cream-color-contorno-cor-toffee | Toffee |

## Notas pipeline V1

- T1: hero com **paleta aberta + B03** (composição 01 do kit)
- Cores dos panos: herdar 100% da ficha da paleta
- T2: macro creme da paleta OU macro cerdas/detalhe do B03
- T3: hands + B03 (quando track liberado)
- Nunca redesenhar packaging; usar packshots de `assets/products/{kit-handle}/`
