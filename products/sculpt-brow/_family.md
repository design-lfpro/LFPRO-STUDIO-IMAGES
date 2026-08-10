---
family: sculpt-brow
title: Sculpt Brow
product_type: Lapiseira para Sobrancelhas
status: dna-v1
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
handles:
  - sculpt-brow-light
  - sculpt-brow-medium
  - sculpt-brow-dark
launch: "2026-08-13"
source: |
  Google Drive — Marketing Interno/17. LAPISEIRAS/SCULPT BROW/
  (FOTO PRODUTO/SITE = packshots + swatches; PARA APROVAR, CARD ENVIO, FOTO MODELO = outros materiais)
  AÇÕES/0813 - SCULPT BROW LANÇAMENTO (campanha)
  Ficha técnica: sculpt brow.pdf (Drive)
---

# Sculpt Brow — DNA de família

Lapiseira retrátil de ponta chanfrada para sobrancelhas. Produto **novo**, lançamento **13/08/2026**. Ainda não está no site (não aparece em `assets/catalog/products-index.json`) — packshots vieram do Drive interno, não do scraping do site.

## Claim central (copy oficial)

"Uma lapiseira retrátil desenvolvida para criar sobrancelhas naturalmente definidas." — ponta chanfrada com **duas funções**: extremidade fina para fios ultrafinos, face mais ampla para preencher falhas.

## Packaging (lock visual)

| Elemento | Lock |
|----------|------|
| **Corpo** | Cilindro preto brilhante (glossy black), retrátil, slim |
| **Texto** | Vertical gold uppercase, duas linhas: `SCULPT BROW` |
| **Logo** | Monograma LF gold, abaixo do texto, próximo à base |
| **Faixa de tom** | Anel/faixa na cor do shade logo acima da base (light = marrom claro, medium = marrom acinzentado médio, dark = marrom profundo acinzentado) |
| **Ponta** | Chanfrada (bevel), cor do tom visível, "uma ponta, duas funções" |
| **Cap** | Tampa preta glossy curta, formato de cúpula no topo, sempre ao lado no packshot |
| **Mecanismo** | Rosca visível logo abaixo da ponta (parte retrátil) |

**Nunca:** trocar "SCULPT BROW" por outro nome, tampa dourada, corpo fosco (é glossy), remover a faixa de cor do tom.

## Três tons (claims oficiais)

| Tom | Descrição oficial | Subtom |
|-----|--------------------|--------|
| **LIGHT** | Marrom claro — fios loiros, castanho claro, ruivos, baixo contraste | Frio |
| **MEDIUM** | Marrom médio — fios castanho médio, morenos, médio contraste | Frio |
| **DARK** | Marrom profundo acinzentado — fios castanho escuro, pretos, alto contraste | Frio |

## Claims de performance (body_text / material de lançamento)

- Efeito fio a fio, acabamento natural, definição precisa, preenchimento uniforme
- Super macia, desliza facilmente, não puxa os fios, esfuma com facilidade
- Resistente à água e à oleosidade, não transfere, acabamento matte natural
- Fórmula anidra clean beauty: 100% vegana, sem fragrância, sem água, sem conservantes
- Ativos: óleo de mamona (hidrata/maciez) + vitamina E (antioxidante)

## Textura / swatch

Traço em curva (scribble), acabamento matte-cremoso, densidade alta mesmo em traço fino. Cor do swatch = cor do shade (ver `02.png` por handle — já é referência de estúdio, fundo bege/nude com sombra dramática).

## Prompt anchors (EN)

```
LF PRO Sculpt Brow retractable brow pencil identity lock: slim glossy black cylindrical
body, gold vertical uppercase wordmark "SCULPT BROW", gold LF monogram near base,
shade-colored ring band above the base, angled/bevel tip in shade color, visible twist
mechanism just below the tip, short glossy black dome cap placed beside the pencil.
Photorealistic, exact packaging from reference image.
```

## Anti-patterns

- Não inventar novo nome de produto ou claim que não está no material oficial
- Não fazer full-face brow makeup proof (T5 bloqueado)
- Não trocar glossy por matte no corpo
- Não confundir com `products/lapis-olhos` (família de lápis para olhos, gel, matte — produto diferente)

## Notas V1

- `01.png` por handle = packshot clean (fundo off-white, produto + tampa, sem swatch) — **identity lock**
- `02.png` por handle = still já em estilo "hero" (fundo bege/nude, sombra dramática, produto + tampa + swatch) — referência de composição pronta, útil como anchor de estilo ecommerce
- Produto pré-lançamento: **não** usar claims além dos listados aqui até o site publicar a ficha oficial
