---
handle: essential-lips-malt
title: "Essential Lips Malt"
family: essential-lips
product_type: "Batom Líquido"
url: "pending-launch-2026-09-09"
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
status: dna-v1-pre-launch
launch_date: 2026-09-09
assets_local: assets/products/essential-lips-malt/
shade: Malt
lipstick_hex_approx: "#A32A3B"
---

# Essential Lips Malt

## Identidade do produto

Essential Lips tom **Malt**. Mesma embalagem da família (tubo translúcido + aplicador doe-foot + tampa preta); diferencia-se pela **cor do líquido** visível no tubo, na ponta do aplicador e no swatch.

- Handle Shopify (previsto): `essential-lips-malt`
- Lançamento oficial: **09/09/2026** — ainda não publicado no site nesta data, não inventar URL/SKU/preço reais
- Imagens locais: 01.png (packshot oficial + swatch, fonte: material de campanha)

## Packaging (lock visual)

Idêntico ao [[_family|DNA da família Essential Lips]]:

- Tubo translúcido/fosco com monograma LF gold + LF PRO
- Tampa preta lisa + aplicador doe-foot em espuma
- **Não alterar** nenhum destes elementos entre tons

## Cor e materiais

| Elemento | Spec |
|----------|------|
| Packaging | ver family |
| Cor do produto | Tom terroso avermelhado profundo (ver nota da família sobre divergência com o documento interno de direcionamento). |
| Hex aproximado (observado no packshot oficial) | `#A32A3B` |

## Logo e tipografia no produto

Monograma LF + LF PRO em gold no corpo do tubo. Sem texto de tom impresso no packaging — tom identificado por naming/comunicação.

## Textura / fórmula visível

Líquido cremoso e fluido, acabamento soft matte aveludado após secagem, filme flexível. Swatch no packshot mostra aplicação em traço largo, opaco, sem transparência.

## Fotografia de estúdio

Packshot oficial: fundo branco puro (cutout), sem sombra própria. Para vídeo social: re-iluminar em **dark-feed** mantendo o mesmo objeto (composição em #0E0E0E).

## Diferenças vs outros tons da linha

| Tom | Handle | Cor (aprox) |
|-----|--------|-------------|
| Beige | essential-lips-beige | `#B96A52` |
| Rose | essential-lips-rose | `#B06B72` |
| Blush | essential-lips-blush | `#C24A73` |
| Malt | essential-lips-malt | `#A32A3B` |
| Mauve | essential-lips-mauve | `#9B4A5E` |
| Clay | essential-lips-clay | `#8E3A34` |
| Carmim | essential-lips-carmim | `#C21F2C` |
| Wine | essential-lips-wine | `#4A1027` |

Este SKU = **Malt**. Não misturar cor de outro handle.

## Prompt anchors (EN)

### Still lock (packshot identity)

```
Exact LF PRO Essential Lips liquid lipstick shade Malt, match reference image packaging 1:1,
frosted translucent tube with gold LF monogram and LF PRO lettering, glossy black cap,
doe-foot foam applicator tip saturated in color #A32A3B, wide lipstick swatch smear behind
product matching shade #A32A3B, pure white ecommerce cutout background, preserve logo, no redesign
```

### Studio hero scene (T1)

```
LF PRO Essential Lips Malt exact packaging from reference on dark charcoal beauty studio
backdrop, soft key + gold rim light, product hero 3/4, micro push-in, 9:16, shade color
#A32A3B visible on applicator/swatch, logo sharp, no face no hands
```

### Texture macro (T2)

```
Macro glossy liquid lipstick smear texture color #A32A3B, soft matte setting finish, creamy
fluid swipe, premium beauty soft focus, shallow DOF, no face
```

## Anti-patterns

- Trocar cor do líquido/aplicador/swatch
- Deformar aplicador doe-foot (não é pincel, é espuma porosa)
- Full-face application (T5)
- Apresentar como garantia universal de "não transfere" sem mencionar tempo de secagem
- Embalagem de outra marca "inspired"

## Claims oficiais (material de lançamento)

> Essential Lips é um batom líquido de alta cobertura que combina cor intensa, acabamento soft matte aveludado e uma sensação confortável nos lábios. Sua textura cremosa e fluida desliza com facilidade e, após a secagem, forma um filme flexível que acompanha os movimentos dos lábios. Alta cobertura, cor intensa, aplicação uniforme, intensidade construível, tecnologia de formação de filme, resistência. Longa duração, resistente à água, conforto absoluto, desempenho premium. Sem parabenos, produto vegano, não testado em animais. Enriquecido com Manteiga de Karité, Manteiga de Cacau, Sílica, Sistema de formação de filme e Copolímero Elastomérico.

> ⚠️ Fonte: material oficial de lançamento (Drive), não o `body_text` do site — produto ainda não publicado em 08/09/2026. Sincronizar com o site assim que o lançamento (09/09/2026) for ao ar.

## Notas para pipeline V1

- Reference obrigatória: `assets/products/essential-lips-malt/01.png`
- Composite dark: extrair produto do fundo branco e colocar em #0E0E0E
- Assim que o Shopify publicar o produto, atualizar `url`, `status` (remover `-pre-launch`) e sincronizar `assets/catalog/*.json`
