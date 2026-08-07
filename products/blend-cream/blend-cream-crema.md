---
handle: blend-cream-crema
title: Blend Cream Crema
family: blend-cream
product_type: Corretivo
url: https://lfpro.com.br/products/blend-cream-crema
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: []
status: dna-v1
assets_local: assets/products/blend-cream-crema/
---

# Blend Cream Crema — DNA v1

> Herda packaging lock de [[_family|Blend Cream]]. Este arquivo fixa **tom / subtom / hex / anchors** específicos.

## Identidade

- **Handle:** `blend-cream-crema`
- **Família:** Blend Cream (6 tons café)
- **Tipo:** Corretivo cremoso alta cobertura em pote
- **Ordem visual na linha:** 1/6
- **Faixa:** TOM CLARO (mais claro da linha) — peles claras
- **Subtom:** TOM CLARO — pale ivory/rosy beige; ideal peles claras (tags catálogo: pele clara / tom claro)
- **Leitura visual 01:** Tom mais claro: ivory rosado pálido, quase porcelana quente-fria; swatch bem claro no 01.
- **Notas tags:** tags: pele clara, peles claras, tom claro

## Packaging lock

Ver [[_family|Blend Cream — packaging lock]]. Resumo:

- Pote redondo transparente/translúcido aberto com **swirl** da fórmula
- Tampa disco **preta fosca** com monograma **LF ouro** + **LF PRO** ouro
- Hero: pote + lid + stroke na cor do tom
- **Sem nome “Crema” na tampa**

## Cores / materiais hex

| Elemento | Hex | Fonte |
|---|---|---|
| Fórmula / swatch (aprox.) | `#F0D9C8` | packshot 01 + subtom |
| Fórmula alt | `#F5E0D2` | highlight |
| Tampa preta | `#0A0A0A` | família |
| Logo ouro | `#C9A84C` | família |
| Fundo hero | `#F7F5F2` | família |

## Logo / tipografia

Idêntico à família no lid. Cards de subtom usam “SUBTOM CREMA” só em overlay de marketing, não no pack físico.

## Textura fórmula

- Cream densa tipo mousse/concealer, cor `#F0D9C8`
- Swirl no pote + stroke opaco semi-mate
- Dry-Flo® (família): toque seco aveludado em uso — no still, creme ainda brilha nas cristas

## Foto estúdio site

- **01:** hero pote aberto + lid + stroke `#F0D9C8`
- **02:** modelo com label do tom (quando presente)
- **03:** stil life subtom (quando presente no asset)
- Cards compartilhados de apelos/fórmula/cartela

## Diferenças deste tom

- Tom mais claro: ivory rosado pálido, quase porcelana quente-fria; swatch bem claro no 01.
- Subtom: Leitura visual: fundo claro levemente rosado/neutro frio (sem card subtom dedicado no asset set)
- Não usar fórmula de outro nome café

## Prompt anchors EN

**Still lock**
```
LF PRO Blend Cream Crema concealer, open round jar with creamy swirl color #F0D9C8, matte black lid with gold interlocking LF monogram and gold LF PRO lettering, very light ivory rosy-beige creamy concealer, fair skin shade, never redesign packaging logo
```

**Studio T1**
```
Studio beauty hero off-white, Blend Cream Crema open jar and black gold-logo lid, thick swatch stroke #F0D9C8 (very light ivory rosy-beige creamy concealer, fair skin shade) behind product, soft shadow, e-commerce packshot
```

**Texture T2**
```
Extreme macro Blend Cream Crema concealer cream #F0D9C8, very light ivory rosy-beige creamy concealer, fair skin shade, dense creamy mousse texture, soft ridges and specular highlights, no glitter
```

## Anti-patterns

- ❌ Confundir com Soft Matte (tubo airless) — este é **pote**
- ❌ Cor de outro tom da linha café
- ❌ Esfriar/esquentar fora do subtom: Leitura visual: fundo claro levemente rosado/neutro frio (sem card subtom dedicado no asset set)
- ❌ Anti-patterns de packaging da família

## Claims do body_text

Mesmos da família (não exclusivos do tom):

- Alta cobertura; olheiras, manchas, imperfeições/acne
- Sem craquelar / sem pesar; construção de camadas
- Lanolina, Vitamina E, Óleo de Girassol
- Dry-Flo® — toque seco, controle de brilho, aveludado, fixação
- Alta fixação e resistência

## Notas V1

- Subtom de crema: inferido do packshot 01 + tags (sem arquivo *-Subtom no set Crema)
- Hex aproximado; preferir `assets/products/blend-cream-crema/01.png` como ground truth de cor
- status: dna-v1
