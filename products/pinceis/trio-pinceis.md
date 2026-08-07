---
handle: trio-pinceis
title: Kit Pincéis
family: pinceis
product_type: Kit
url: https://lfpro.com.br/products/trio-pinceis
sku: "12744"
price: "242.70"
preferred_tracks:
  - T1-product-hero
  - T3-tools-hands
blocked_tracks:
  - T5-face-proof
status: ready
assets_local: assets/products/trio-pinceis/
---

# Kit Pincéis (Trio)

Conjunto completo de pele: **F01 + C02 + B03**. Um kit, três formas de cabeça distintas, mesma linguagem visual preto + gold + cerdas dual-tone.

---

## Identidade

| Campo | Valor |
|-------|-------|
| Tipo | Kit (3 tools) |
| Conteúdo | [[pincel-para-base-f01\|F01]] + [[pincel-de-corretivo-c02\|C02]] + [[pincel-duplo-blush-e-iluminador-b03\|B03]] |
| Promessa | Pele completa com 3 pincéis (base → corretivo → blush/iluminador) |
| Visual hero | Flatlay cruzado dos três em off-white (asset `01`) |

### Checklist de legibilidade no kit

Cada tool deve permanecer **distinguível**:

| Tool | Silhueta rápida |
|------|-----------------|
| F01 | Single, cabeça **angular** larga, pescoço cônico flare |
| C02 | Single, cabeça **dome** pequena, cabo fino |
| B03 | **Duplo**, ampulheta, duas cabeças |

Se o viewer não identifica os três códigos, o lock falhou.

---

## Packaging / objeto lock

### Composição kit (objeto “kit”)

- Não há embalagem box obrigatória no packshot principal — o “produto” visual é o **trio de tools**.
- Asset `01`: três pincéis cruzados em X/asterisco sobre fundo off-white; B03 no centro diagonal com logo gold legível; F01 e C02 com códigos no cabo.
- Cada item herda 100% o lock da ficha individual (cerdas, ferrule, gravação).

### Cerdas / cabos / logos

- Aplicar locks de `_family.md` + fichas F01/C02/B03 sem exceção.
- No kit, **não homogenizar** as cabeças (erro comum de IA: três domes iguais).
- Gold logos em todos; códigos `F01`, `C02`, `B03` legíveis quando o cabo estiver em foco.

### Assets do handle

| File | Conteúdo | Nota |
|------|----------|------|
| `01.png` | Flatlay trio cruzado off-white | **T1 kit lock** |
| `02.png` | (reuso) F01 em uso rosto | ref only |
| `03.png` | (reuso) F01 packshot | pode servir de cutaway |
| `04.png` | (reuso) C02 em uso | ref only |
| `05.png` | (reuso) C02 packshot | cutaway |
| `06.png` | (reuso) B03 + paleta | T3 |
| `07.png` | (reuso) B03 packshot | cutaway |

---

## Cores hex

Idênticas à família (`_family.md`):

| Uso | Hex |
|-----|-----|
| Black tools | `#0A0A0A` |
| Cerda tip / base | `#F2F2F2` / `#141414` |
| Gold logo | `#C9A84C` / `#D4AF37` |
| Fundo ecommerce | `#F7F5F2` |
| Dark-feed | `#000000` |

---

## Logo

- Três gravações gold independentes — cada cabo com seu monograma + código.
- No flatlay kit, priorizar legibilidade do **B03** (centro) e ao menos um código F01/C02.

---

## Textura

- Contraste das três densidades de cabeça no mesmo frame = story visual do kit.
- Superfícies: gloss ferrule + matte handle + soft bristles em todos.

---

## Foto estúdio

- **Hero kit:** `01.png` (composição cruzada).
- Cutaways: packshots individuais dos três handles.
- T3: mão com um tool por vez, ou mãos organizando os três em superfície preta/off-white — **sem full face**.

---

## Prompt anchors EN

### Still — kit identity lock

```text
LF PRO trio brush kit flat lay: three professional black makeup brushes crossed on off-white
background #F7F5F2 — (1) F01 angular slanted dense dual-tone foundation brush, (2) C02 small
rounded dome concealer brush, (3) B03 double-ended hourglass blush highlighter brush with two heads,
all with white-tip-to-black-base synthetic bristles, gold foil LF PRO logos and codes F01 C02 B03
readable, soft studio shadow, premium ecommerce product photography, clearly distinct brush head shapes
```

### T1 hero — dark-feed

```text
three LF PRO brushes F01 C02 B03 floating or arranged on pure black, warm gold rim light,
distinct silhouettes angular vs dome vs double-ended, gold engravings catching light,
luxury beauty kit commercial still
```

### T3 hands-in-use (SEM rosto full)

```text
elegant hands arranging three LF PRO brushes on dark surface, only hands and tools in frame,
F01 angular head, C02 dome head, B03 dual heads clearly different, gold logos visible,
nude manicure, beauty commercial, no face
```

```text
hand selecting B03 dual brush from the trio set, other two brushes resting nearby,
dark studio warm bokeh, no full face
```

---

## Anti-patterns

- Três pincéis visualmente idênticos
- Omitir B03 double-ended (kit “vira” dois single + erro)
- Embalagem inventada (caixa genérica, fita, etc.) se não estiver no packshot
- Full-face rotina de make com os três (T5)
- Claims de desconto/“de R$ X por Y” inventados

---

## Claims site

Fonte: `body_text` Shopify.

- 3 pincéis para acabamento uniforme, aplicação precisa e performance em todas as etapas da pele.
- Composto por **Pincel para Base F01**, **Pincel para Corretivo C02** e **Pincel Duplo Blush e Iluminador B03**.
- Da construção da pele à finalização com blush e iluminador.
- **Pele completa com apenas 3 pincéis.**
- Mais precisão por formato; acabamento uniforme (duplo polimento); menor desperdício (densidade); praticidade; performance profissional.

---

## Notas V1

- Kit = ótimo T1 “product constellation”; cuts para close de cada cabeça.
- Sempre linkar locks das fichas filhas — não reescrever geometria aqui.
- Preço kit no catálogo: R$ 242,70 (soma dos singles); não inventar promo.
- Assets reutilizam frames dos singles — preferir `trio-pinceis/01.png` como hero de kit e `assets/products/{sku}/01.png` para cutaways fiéis.
