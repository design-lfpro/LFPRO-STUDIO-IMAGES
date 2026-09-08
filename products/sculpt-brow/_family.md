---
family: sculpt-brow
title: "Linha Sculpt Brow"
product_type: "Lapiseira para Sobrancelha"
handles: [sculpt-brow-light, sculpt-brow-medium, sculpt-brow-dark]
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
status: dna-v1-pre-launch
launch_date: 2026-09-09
source: "Material oficial de lançamento (Google Drive), site ainda não publicado nesta data"
updated: 2026-09-08
---

# Família Sculpt Brow — DNA compartilhado

## Identidade

Lapiseira retrátil para sobrancelhas, ponta chanfrada de dupla função, 3 tons. **Lançamento oficial: 09/09/2026.** Ainda não está no site (lfpro.com.br) nem no Shopify na data desta ficha — dados vêm dos materiais de campanha oficiais da marca (PDF de lançamento + packshots), não do `body_text` do site. Sincronizar com a ficha real do Shopify assim que publicado.

## Packaging lock (NUNCA redesenhar)

Observado nos packshots oficiais (`01.png` de cada tom):

### Componentes

1. **Corpo (barrel)**
   - Cilíndrico, fino, preto fosco/laqueado
   - Wordmark **SCULPT BROW** em gold, orientação vertical, ao longo do corpo
   - **Monograma LF gold** pequeno, abaixo do wordmark
   - Anel/faixa colorida fina próxima à ponta, indicando o tom (cor varia por SKU)

2. **Ponta**
   - Mina retrátil com **ponta chanfrada** (bisel diagonal) — permite traço fino com a lateral e preenchimento com a face larga
   - Cor da mina varia conforme o tom

3. **Tampa**
   - Cilíndrica, preto brilhante, topo levemente arredondado, sem texto — apresentada separada do corpo no packshot

### Fotografia (gramática)

- Fundo: off-white/cinza muito claro, seamless, luz suave uniforme
- Composição still: produto aberto (mina exposta) + tampa separada ao lado, alinhados horizontalmente
- Sem sombra dramática, sem props, sem mão/rosto no still de identidade

## Cores de packaging (fixas — não variam por tom)

| Elemento | Hex aprox |
|----------|-----------|
| Corpo / tampa | `#0A0A0A` preto fosco/laqueado |
| Wordmark / logo | `#C9A227`–`#E1C46A` gold |
| Fundo packshot | off-white `#F5F4F1` |

## Os 3 tons (mina, não packaging)

| Tom | Handle | Descrição oficial | Uso indicado |
|-----|--------|--------------------|--------------|
| Light | sculpt-brow-light | Marrom claro, subtom frio | Fios loiros, castanho claro, ruivos, baixo contraste |
| Medium | sculpt-brow-medium | Marrom médio, subtom frio | Fios castanho médio, morenos, médio contraste |
| Dark | sculpt-brow-dark | Marrom profundo acinzentado, subtom frio | Fios castanho escuro, pretos, alto contraste |

A faixa colorida no corpo do lápis muda de acordo com o tom (mais clara em Light, mais escura/acinzentada em Dark).

## Claims oficiais (material de lançamento — sincronizar com body_text do site assim que publicado)

> Uma lapiseira retrátil desenvolvida para criar sobrancelhas naturalmente definidas. Sua ponta chanfrada permite desenhar fios ultrafinos ou preencher falhas com rapidez, proporcionando um resultado preciso, elegante e profissional.
>
> Uma ponta, duas funções: use a extremidade fina para desenhar fios ultrafinos, ou a face mais ampla para preencher falhas com rapidez e naturalidade. Formato impecável: após o uso, basta pressionar suavemente a ponta contra uma superfície plana para remodelar o formato chanfrado.
>
> Efeito fio a fio, acabamento natural, definição precisa, preenchimento uniforme, resultado rápido, acabamento profissional.
>
> Alta performance: super macia, desliza facilmente, não puxa os fios, esfuma com facilidade, resistente à água, resistente à oleosidade, não transfere, acabamento matte natural.
>
> Ativos: Óleo de Mamona (hidrata e promove maciez), Vitamina E (ação antioxidante e proteção). Fórmula anidra clean beauty: 100% vegana, sem fragrância, sem água, sem conservantes.

## Prompt anchors (EN) — família

### Still lock (identity)

```
Exact product packaging match to reference photo: LF PRO Sculpt Brow retractable eyebrow
pencil, slim matte black barrel, vertical gold SCULPT BROW wordmark and small gold LF
monogram, angled chiseled tip with brown lead exposed, matching glossy black cap shown
separately alongside, soft off-white seamless background, preserve logo sharpness, no redesign
```

### Studio hero T1 (dark feed)

```
Same exact Sculpt Brow pencil packaging as reference, product hero on dark charcoal
seamless background #0E0E0E, soft beauty key light + subtle gold rim, micro push-in,
9:16 commercial, logo and chiseled tip perfectly preserved, no hands, no face
```

### Texture macro T2

```
Extreme macro of chiseled brow pencil tip texture matching reference lead color, fine
matte brow strokes fanning out like hair-strokes on light backdrop, premium beauty,
shallow depth of field, no face, packaging only if partial in frame with correct gold black design
```

## Anti-patterns família

- Logo prata/branco ou wordmark horizontal (é sempre vertical no corpo)
- Ponta redonda/normal (a mina é **chanfrada**, nunca cilíndrica lisa)
- Trocar a cor da faixa indicadora de tom entre SKUs
- Full-face application (T5)

## Notas pipeline V1

- **Pré-lançamento (até 09/09/2026):** usar apenas os assets aqui documentados (Drive interno). Não existe ainda URL pública nem SKU/ID Shopify — não inventar esses dados.
- Após o lançamento: sincronizar `url`, `id` Shopify, preço e `variants` reais assim que o produto for publicado (ver `assets/catalog/products-index.json` para o padrão de outros produtos).
- Golden path recomendado para demos: **Medium** (tom mais versátil/central da linha)
- Usar `01.png` (packshot produto isolado) como reference obrigatória por tom
