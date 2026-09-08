---
handle: sculpt-brow-medium
title: "Sculpt Brow Medium"
family: sculpt-brow
product_type: "Lapiseira para Sobrancelha"
url: "pending-launch-2026-09-09"
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
status: dna-v1-pre-launch
launch_date: 2026-09-09
assets_local: assets/products/sculpt-brow-medium/
shade: Medium
---

# Sculpt Brow Medium

## Identidade do produto

Sculpt Brow tom **Medium**. Mesma embalagem da família (corpo preto + wordmark vertical gold + ponta chanfrada); diferencia-se pela **cor da mina** e pela faixa indicadora de tom no corpo.

- Handle Shopify (previsto): `sculpt-brow-medium`
- Lançamento oficial: **09/09/2026** — ainda não publicado no site nesta data, não inventar URL/SKU/preço reais
- Imagens locais: 01.png (packshot oficial, fonte: material de campanha)

## Packaging (lock visual)

Idêntico ao [[_family|DNA da família Sculpt Brow]]:

- Corpo preto fosco/laqueado com wordmark SCULPT BROW vertical em gold + monograma LF
- Ponta chanfrada, tampa preta separada no still
- **Não alterar** nenhum destes elementos entre tons

## Cor e materiais

| Elemento | Spec |
|----------|------|
| Packaging | ver family |
| Cor da mina | Marrom médio, subtom frio. |
| Uso indicado | Ideal para fios castanho médio, morenos e de médio contraste. |

## Logo e tipografia no produto

Wordmark **SCULPT BROW** vertical em gold ao longo do corpo + monograma LF gold abaixo. Sem texto de tom impresso — tom identificado pela faixa colorida próxima à ponta e por naming/comunicação.

## Textura / fórmula visível

Mina anidra, fórmula clean beauty (100% vegana, sem fragrância, sem água, sem conservantes). Acabamento matte natural, efeito fio a fio ao aplicar.

## Fotografia de estúdio

Packshot oficial: fundo off-white seamless, luz suave, produto + tampa lado a lado. Para vídeo social: re-iluminar em **dark-feed** mantendo o mesmo objeto (composição em #0E0E0E).

## Diferenças vs outros tons da linha

| Tom | Handle | Descrição |
|-----|--------|-----------|
| Light | sculpt-brow-light | Marrom claro, subtom frio. |
| Medium | sculpt-brow-medium | Marrom médio, subtom frio. |
| Dark | sculpt-brow-dark | Marrom profundo acinzentado, subtom frio. |

Este SKU = **Medium**. Não misturar cor de mina de outro handle.

## Prompt anchors (EN)

### Still lock (packshot identity)

```
Exact LF PRO Sculpt Brow retractable eyebrow pencil shade Medium, match reference image
packaging 1:1, matte black barrel with vertical gold SCULPT BROW wordmark and small gold
LF monogram, angled chiseled tip with medium brown lead exposed, matching glossy
black cap shown separately, soft off-white seamless background, preserve logo, no redesign
```

### Studio hero scene (T1)

```
LF PRO Sculpt Brow Medium exact packaging from reference on dark charcoal beauty studio
backdrop, soft key + gold rim light, product hero 3/4, micro push-in, 9:16, medium
brown lead tip visible, logo sharp, no face no hands
```

### Texture macro (T2)

```
Macro chiseled brow pencil tip texture, medium brown lead, fine matte hair-stroke
marks on light backdrop, premium beauty soft focus, shallow DOF, no face
```

## Anti-patterns

- Trocar cor da mina/faixa indicadora
- Ponta redonda/lisa (deve ser sempre chanfrada)
- Full-face application (T5)
- Embalagem de outra marca "inspired"

## Claims oficiais (material de lançamento)

> Uma lapiseira retrátil desenvolvida para criar sobrancelhas naturalmente definidas. Ponta chanfrada de dupla função: extremidade fina para fios ultrafinos, face ampla para preencher falhas com rapidez e naturalidade. Super macia, desliza facilmente, não puxa os fios, esfuma com facilidade, resistente à água, resistente à oleosidade, não transfere, acabamento matte natural. Enriquecida com Óleo de Mamona e Vitamina E. Fórmula anidra clean beauty: 100% vegana, sem fragrância, sem água, sem conservantes.

> ⚠️ Fonte: material oficial de lançamento (Drive), não o `body_text` do site — produto ainda não publicado em 08/09/2026. Sincronizar com o site assim que o lançamento (09/09/2026) for ao ar.

## Notas para pipeline V1

- Reference obrigatória: `assets/products/sculpt-brow-medium/01.png`
- Composite dark: extrair produto do fundo off-white e colocar em #0E0E0E
- Assim que o Shopify publicar o produto, atualizar `url`, `status` (remover `-pre-launch`) e sincronizar `assets/catalog/*.json`
