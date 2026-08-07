---
handle: primer-labial
title: Primer Labial
family: primer-labial
product_type: Primer
sku: "1078"
price: "59.90"
url: https://lfpro.com.br/products/primer-labial
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
status: dna-v1
assets_local: assets/products/primer-labial/
---

# Primer Labial

## Identidade do produto

Primer/hidratante labial em tubo soft-squeeze branco com bico aplicador. Ativos: Vitamina E, Pró-vitamina B5, D-Pantenol. 10 g. Dermatologicamente testado; cruelty free; sem glúten.

## Packaging (lock visual) — NUNCA redesenhar

| Elemento | Lock |
|----------|------|
| **Formato** | Tubo plástico branco cilíndrico-cônico com nozzle branco alongado (doe-foot style tip) |
| **Cap** | Tampa branca canelada (ribbed screw cap) no topo |
| **Logo** | Monograma **LF** grande em **prata/grafite** (`#8A8A8A`–`#A0A0A0`) + wordmark **LF PRO** abaixo — **NÃO dourado** neste SKU |
| **Título** | `PRIMER LABIAL` bold cinza escuro |
| **Claims pack** | “Contra Rachaduras, Ressecamento e Antioxidante”; “Super Hidratante Vitamina E e Pró Vitamina B5” |
| **Bullets mint** | Lista com check em teal/mint: DISFARCE ÓPTICO · LÁBIOS SAUDÁVEIS · CALMANTE |
| **Faixa** | Diagonal teal/mint `#5BB8A8` / `#4AA89A` no canto inferior direito |
| **Net** | `10g` |
- Fundo packshot: off-white
- 02: lifestyle modelo aplicando (referência T4 futura)

## Cores e materiais

| Parte | Spec |
|-------|------|
| Tubo/cap/nozzle | Branco opaco `#FAFAFA` |
| Logo | Prata/grafite (não gold) |
| Texto principal | Cinza escuro `#333` |
| Acento | Teal mint `#5BB8A8` |
| Fórmula (saída) | Translúcido/claro hidratante |

## Logo e tipografia no produto

- Monograma LF **prata** (exceção vs makeup black-gold)
- LF PRO prata
- Copy em PT no pack; não traduzir no redesign

## Textura / fórmula visível

- Textura leve, não pegajosa (claim)
- No lifestyle: brilho hidratante natural nos lábios, sem cor opaca

## Fotografia de estúdio do site

- 01: tubo vertical solo, off-white, soft shadow
- 02: modelo aplicando com nozzle nos lábios (T4 ref; V1 não usa como identity se logo ilegível)

## Diferenças vs outras linhas

- Única embalagem branca+teal desta leva de fichas
- Logo prata, não gold
- Categoria skincare/prep labial, não cor

## Prompt anchors (EN)

### Still lock (packshot identity)
```
Exact LF PRO Primer Labial tube. White squeeze tube with white ribbed cap and white elongated nozzle tip. Large silver/grey LF monogram and LF PRO. Text "PRIMER LABIAL", claims about cracks/dryness/antioxidant, Vitamin E and Pro Vitamin B5. Mint teal checkmarks: optical blur, healthy lips, calming. Mint diagonal accent, 10g. Off-white #F7F5F2 background, soft studio light. Photorealistic identity lock. Silver logo NOT gold.
```

### Studio hero scene (T1)
```
9:16 clean beauty product hero, white LF PRO lip primer tube floating on soft off-white or gentle grey, mint accent light, premium skincare commercial, slow elegant rotation, identity locked packaging.
```

### Texture macro (T2)
```
Macro clear/translucent hydrating lip primer gel on lips or on surface, non-sticky glossy sheen, soft dewy texture, beauty skincare advertising macro, no opaque color product.
```

## Anti-patterns

- **Não** usar monograma dourado (este SKU é prata)
- Não tubo preto
- Não transformar em gloss colorido
- Não omitir faixa mint / bullets
- Não full-face V1
- Não inventar FPS ou “preenchedor de lábios com ácido” fora do body_text

## Claims oficiais (body_text)

- Lábios macios e hidratados; textura leve e não pegajosa
- Vitamina E (hidratante e antioxidante)
- Pró Vitamina B5 (umectante; barreira cutânea)
- D-Pantenol (hidratante; cicatrizante e anti-inflamatório)
- Previne/trata linhas finas; combate ressecamento e rachaduras; ação calmante e regeneradora; alívio imediato
- 10 g; dermatologicamente testado; cruelty free; sem glúten

## Notas para pipeline V1

- Âncora: `assets/products/primer-labial/01.png`
- style_override: preferir **white-ecommerce / clean** em vez de dark-feed agressivo (pack é branco)
- T2: textura gel translúcido, não swatch de cor
