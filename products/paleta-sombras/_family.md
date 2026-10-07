---
family: paleta-sombras
title: Paletas de Sombras
product_type: Sombra
status: dna-v1
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
handles:
  - paleta-de-sombras-vital
  - paleta-de-sombras-energica
  - paleta-de-sombras-stone    # lançamento out/26 = Vital renomeada
  - paleta-de-sombras-sunset   # lançamento out/26 = Enérgica renomeada
  - paleta-de-sombras-petal    # lançamento out/26, paleta nova (rosados)
  - paleta-de-sombras-basic    # lançamento out/26, paleta nova (marrons)
---

# Paletas de Sombras — DNA de família

Duas paletas 6 pan (2×3) em compacto preto: **Vital** (tons frios) e **Enérgica** (tons quentes). 5 opacos + 1 cintilante. 12 g. Vegano / cruelty free.

## Packaging (lock visual)

| Elemento | Lock |
|----------|------|
| **Tampa fechada** | Compacto preto matte/soft-gloss quadrado; monograma LF gold grande central + LF PRO gold abaixo |
| **Interior** | 6 godets retangulares arredondados em grade 2×3; espelho na tampa interna (visível quando aberta em ângulo) |
| **Layout 01** | Tampa fechada à esquerda + paleta aberta à direita (ligeiramente sobreposta) |
| **Layout 02** | Paleta aberta top-down + swatches de pó esmagado em faixas diagonais ao fundo |

## Diferença de família de cor

| Paleta | Temperatura | Pans (aprox.) |
|--------|-------------|---------------|
| **Vital** | Fria | Preto, bordô, marrom frio, cinza, rose taupe matte, branco/champagne shimmer |
| **Enérgica** | Quente | Coral rosado, marrom chocolate, terracota ferrugem / pêssego rosado claro (único cintilante), terracota tan, nude rosado |

## Claims

- Pigmentação intensa; textura suave/amanteigada ou cremosa
- Pigmentos nobres (Enérgica: ultramicronizados); fácil de esfumar; construção em camadas
- Compacta e elegante; 12 g; vegano e cruelty free

## Prompt anchors (EN)

```
LF PRO eyeshadow palette identity lock: black square compact, large gold LF monogram and LF PRO on lid. Open 6-pan 2x3 grid. Off-white background. Photorealistic, exact pans colors per SKU.
```

## Anti-patterns

- Não inverter Vital ↔ Enérgica
- Não adicionar pans / mudar grade
- Não logo prata
- Não full-eye look como prova de cor V1 sem protocolo

## Notas V1

- 01 = hero packaging; 02 = texture/swatch paradise para T2

## Lançamento out/2026: SUNSET · STONE · PETAL · BASIC

Confirmado pelo cliente (07/10/2026): **o compacto é idêntico** ao das paletas antigas.

| Nova | = Antiga | Cores | Peso | EAN | Status |
|------|----------|-------|------|-----|--------|
| **STONE** | Vital | iguais à Vital (fria) | 12 g | 7898715201958 | pronta p/ geração |
| **SUNSET** | Enérgica | iguais à Enérgica (quente) | 12 g | 7898715201941 | pronta p/ geração |
| **PETAL** | (nova) | rosados, 2 cintilantes | 11 g | 7898715202054 | cores por ref do cliente |
| **BASIC** | (nova) | marrons, 1 cintilante | 11 g | 7898715201934 | cores por ref do cliente |

- **ALLURE (ex-AURA) fica fora deste lançamento** (decisão do cliente). Cartucho creme, outra linha. Não usar.
- Cartucho novo: preto + hot stamping gold (Pantone 871 C); claims **Esfuma Fácil · Alta Pigmentação · Toque Aveludado**
- Nome da paleta **só** no cartucho/adesivo, nunca na tampa
- Refs de cartucho/adesivo: `assets/refs/paletas/lancamento-sunset-stone-petal/`
- Fontes Drive: `Cartucho Paleta - SUNSET.pdf`, `Cartucho Paleta - STONE.pdf`, `Cartucho Paleta de Sombras - PETAL.pdf`, `Adesivo Paleta - *.pdf`, `DIZERES DE ROTULAGEM PALETA DE SOMBRAS SUNSET E STONE.docx`
- Registro das fotos geradas: [`lancamento-out26-fotos.md`](lancamento-out26-fotos.md)

### Regras de foto do lançamento (cliente, 07/10/2026)

- Fundo **sempre preto puro**. **Sem mármore**, pedra ou superfície texturizada.
- Textura do pó = a das fotos reais da Vital/Enérgica (prensado liso e aveludado). Cintilância só nos godets indicados, com micro partículas sutis.
- Gerar **uma foto por vez** e mostrar ao cliente antes da próxima.

### Elementos na biblioteca do Magnific (produto)

Criados em 07/10/2026 a partir das fotos oficiais do site (Drive `FOTO PRODUTO/FOTO SITE`, salvas como `assets/products/{handle}/01.png`). Usar como reference `type: product` com o id numérico:

| Paleta | Elemento | id |
|--------|----------|----|
| PETAL | `LFPRO-Paleta-PETAL` | 2366895 |
| BASIC | `LFPRO-Paleta-BASIC` | 2366896 |
| STONE | `LFPRO-Paleta-STONE` | 2366897 |
| SUNSET | `LFPRO-Paleta-SUNSET` | 2366898 |
