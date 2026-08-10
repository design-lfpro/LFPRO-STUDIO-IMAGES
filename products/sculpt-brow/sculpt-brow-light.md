---
handle: sculpt-brow-light
title: Sculpt Brow Light
family: sculpt-brow
product_type: Lapiseira para Sobrancelhas
sku: null
price: null
url: null
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
status: dna-v1
assets_local: assets/products/sculpt-brow-light/
shade: Light
launch: "2026-08-13"
---

# Sculpt Brow Light

## Identidade do produto

Lapiseira retrátil de ponta chanfrada para sobrancelhas, tom **Light** (marrom claro, subtom frio). Ideal para fios loiros, castanho claro, ruivos e de baixo contraste.

## Packaging (lock visual)

- Corpo preto glossy, cilíndrico, retrátil
- Texto gold vertical: **SCULPT BROW**
- Monograma LF gold próximo à base
- Faixa/anel de cor light (marrom claro) acima da base
- Ponta chanfrada marrom clara, mecanismo de rosca visível
- Cap preto glossy curto, cúpula no topo, sempre ao lado no packshot
- Fundo off-white no packshot oficial

## Cores e materiais

| Parte | Spec |
|-------|------|
| Corpo/cap | Preto glossy |
| Tipografia/logo | Ouro |
| Faixa de tom / ponta / swatch | Marrom claro, subtom frio |

## Textura / fórmula visível

Traço em curva (scribble) matte-cremoso, alta densidade mesmo em linha fina; cor marrom clara consistente com a ponta.

## Fotografia disponível

- `01.png` — packshot clean, fundo off-white, produto + tampa (identity lock)
- `02.png` — still hero já pronto, fundo bege/nude, sombra dramática, produto + tampa + swatch em curva (referência de composição/estilo)

## Prompt anchors (EN)

### Still lock
```
Exact LF PRO Sculpt Brow Light retractable brow pencil. Slim glossy black cylindrical
body, gold vertical wordmark "SCULPT BROW", gold LF monogram near base, light brown
(cool undertone) shade ring band above the base, angled bevel tip in light brown,
visible twist mechanism below the tip. Short glossy black dome cap beside the pencil.
Off-white background, soft studio light. Photorealistic identity lock.
```

### Studio hero (T1)
```
9:16 luxury cosmetics hero shot, LF PRO Sculpt Brow Light retractable pencil standing
upright on a warm nude/beige studio surface, soft dramatic contact shadow, cap resting
beside it, subtle light brown scribble swatch stroke in the background, gold lettering
catching the light, premium beauty commercial photography, packaging fully visible,
no hands, no face.
```

### Texture macro (T2)
```
Macro shot of a light brown brow pencil scribble stroke, matte-creamy pigment texture,
soft sheen, fine hair-like fiber lines visible, beauty advertising macro, cool undertone.
```

## Anti-patterns

- Não trocar "SCULPT BROW" por outro nome
- Não alterar o tom Light para outra cor
- Não corpo matte (é glossy)
- Não full-face brow makeup proof (V1 bloqueado)

## Claims oficiais (material de lançamento)

- Sobrancelhas definidas com efeito natural
- Uma ponta, duas funções: fios ultrafinos ou preenchimento de falhas
- Efeito fio a fio, acabamento natural, definição precisa, resultado rápido
- Super macia, desliza facilmente, não puxa os fios, esfuma com facilidade
- Resistente à água e à oleosidade, não transfere, acabamento matte natural
- Fórmula anidra: 100% vegana, sem fragrância, sem água, sem conservantes
- Óleo de mamona (hidrata/maciez) + vitamina E (antioxidante)
- Ideal para fios loiros, castanho claro, ruivos e de baixo contraste

## Notas para pipeline V1

- Âncora: `assets/products/sculpt-brow-light/01.png` (identity lock, sem swatch)
- `02.png` já é um still em estilo hero pronto — pode servir de referência direta de composição/luz para o still-engineer (Sofia), não só como texture macro
