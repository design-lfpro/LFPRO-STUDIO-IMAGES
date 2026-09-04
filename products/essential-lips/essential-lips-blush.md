---
handle: essential-lips-blush
title: Essential Lips Blush
family: essential-lips
product_type: Batom líquido matte
sku: null
price: "69.90"
url: null
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
status: dna-v1
assets_local: assets/products/essential-lips-blush/
shade: Blush
---

# Essential Lips Blush

## Identidade do produto

Batom líquido matte Essential Lips, tom **Blush** — pink-vermelho vibrante, o mais 'pink' da cartela. Mesmo packaging da linha (ver [[_family|Essential Lips DNA]]); diferencial exclusivo = cor do líquido.

## Packaging (lock visual)

Ver `_family.md`. Lock:

1. Frasco em vidro/acrílico fosco translúcido, colunar, ombros retos — líquido Blush visível por trás do fosco
2. Tampa preta cilíndrica com rosca/grip horizontal no topo
3. Monograma **LF** dourado + wordmark **LF PRO** dourado no corpo do frasco (zona ~65,94×55mm), abaixo do colarinho de duas linhas
4. Aplicador doefoot preto com ponta em veludo/esponja afunilada, cor Blush
5. Sem texto do nome do tom impresso no frasco

**Assets:** `assets/products/essential-lips-blush/01.jpeg` (still de estúdio — fundo cinza, ver aviso de fundo em `_family.md`).

## Cor

**Descrição oficial (fonte: Direcionamento Time Essential Lips):** Tom rosa médio, vibrante. Com fundo levemente quente.

### Leitura aproximada do still de estúdio (hex direcional)

| Parte | Cor / hex aprox |
|-------|-------------------|
| Líquido / swatch Blush | pink-vermelho vibrante, o mais 'pink' da cartela, aprox `#922242` |
| Cap / frasco | packaging padrão da linha — preto + dourado, ver `_family.md` |

**Método:** hex lido por amostragem de pixel da ponta do aplicador em `01.jpeg` (fundo cinza de estúdio, luz não calibrada) — é uma referência direcional, não um Pantone oficial. Validar contra swatch físico ou still com card de cor antes de travar produção final.

## Claims oficiais

Herdados de `_family.md` (seção "Claims e guardrails de comunicação") — válidos para todos os tons: soft matte / acabamento aveludado, alta cobertura buildável, conforto e filme flexível, fórmula com Karité e Cacau, longa duração como posicionamento (sem quantificar horas), resistência à água/transferência como característica técnica (sem promessa absoluta), vegano, sem parabenos, não testado em animais. **Nenhum claim específico de tom além da cor.**

## Anti-patterns

- Ver `_family.md` (lista global)
- mais vibrante/quente que Rose; não confundir com Carmin (Carmin é mais para o vermelho puro, menos rosa)

## Notas para pipeline V1

- Packshot âncora: `assets/products/essential-lips-blush/01.jpeg`
- preferred_tracks: T1 + T2; style_override default dark-feed para vídeo social
- Antes do still final: rodar Ana Produto sobre `01.jpeg` para lock list 1:1 e recompor fundo (still-fonte é cinza de estúdio, não é o fundo final)
