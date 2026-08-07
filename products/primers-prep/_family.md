---
family: primers-prep
title: Primers / Prep de Pele (Makeup Primer)
product_type: Hidratante (catálogo) / Primer (packaging + uso real)
handles:
  - acqua
  - blur
  - luminous
  - radiance
status: dna-v1
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
---

# Primers-Prep — DNA da família

Linha de **prep de pele / makeup primer** LF PRO em **tubo preto alto brilho + ouro**. No Shopify o `product_type` aparece como **Hidratante**, mas o packaging imprime **MAKEUP PRIMER** e as tags incluem primer / pré-make. **Tratar como prep de pele (primer)**, não como hidratante de prateleira skincare DERMA.

Quatro SKUs:

| SKU | Função | Net | Subtítulo no tubo |
|-----|--------|-----|-------------------|
| **Acqua** | Gel hidratante facial matte/fresco — peles oleosas | 35g | GEL HIDRATANTE FACIAL |
| **Blur** | Primer soft focus / poros / matte | 35g | PRIMER FACIAL |
| **Luminous** | Hidratante iluminador facial | 35g | HIDRATANTE ILUMINADOR FACIAL |
| **Radiance** | Prep área dos olhos | **25g** | HIDRATANTE ILUMINADOR ÁREA DOS OLHOS |

## Lock visual compartilhado (NUNCA redesenhar)

### Arquitetura

1. **Tubo** — plástico **preto piano** (high-gloss), formato squeeze com ombro cônico e **tampa flip/long black cap** na base (cap inferior alongado no packshot).
2. **Logo** — monograma **LF** gold grande no topo do painel frontal.
3. **Categoria** — **MAKEUP PRIMER** em gold, duas linhas, caixa alta, tracking largo (comum aos 4).
4. **Nome do produto** — ACQUA / BLUR / LUMINOUS / RADIANCE em gold, maior, caixa alta.
5. **Subtítulo funcional** — linha menor em gold (gel hidratante / primer facial / etc.).
6. **Net weight** — 35g ou 25g (Radiance) em gold, base do painel.
7. **Sem** linha DERMA branca neste pack (isso é skincare Derma).

### Gramática fotográfica

| Tipo | Fundo | Notas |
|------|-------|-------|
| **01 Hero** | Off-white #FAFAF8 | Tubo vertical isolado |
| **02 Beauty** | Escuro / water / wet skin | Modelo com produto (Acqua wet look) |
| **03 Studio dark** | Preto + fumaça/atmosfera | Product float (Blur smoke) |
| Texture | Às vezes gel/creme squeeze | T2 |

## Claims por SKU (resumo site)

**Acqua:** gel ultraleve; matte natural; rápida absorção; peles oleosas; D-Pantenol, quinoa, manga.  
**Blur:** soft focus; silicones; suaviza poros/linhas; controle oleosidade; durabilidade da make.  
**Luminous:** hidratação + viço; cranberry, rosa branca, óleo semente de uva; prep luminoso.  
**Radiance:** contorno olhos; Argireline, colágeno, D-Pantenol, algodão, macadâmia; prep para corretivo.

## Prompt anchors (EN)

### Packaging lock shared

```
LF PRO MAKEUP PRIMER black high-gloss squeeze tube, warm gold foil monogram LF at top, gold uppercase MAKEUP PRIMER stacked, gold product name, gold functional subtitle, gold net weight at bottom, long black cap base, luxury Brazilian cosmetics black-and-gold, never white DERMA bottle
```

### Studio hero

```
black makeup primer tube upright on seamless off-white #FAFAF8, soft diffused light, gentle shadow, front label fully legible gold on black, photorealistic ecommerce packshot
```

### Anti-patterns

- Embalagem branca DERMA (skincare limpeza/sérum)
- Esquecer “MAKEUP PRIMER” no painel
- Radiance com 35g (é **25g**)
- Inventar pump dourado tipo base Soft Matte
- Claims de FPS ou ácido salicílico (outras linhas)
- Face before/after inventado

## SKUs

- [[acqua]] · [[blur]] · [[luminous]] · [[radiance]]

## Notas pipeline V1

- Catálogo type=Hidratante **≠** comunicação: packaging = primer
- T1: 01 packshot branco; dark-feed pode usar 03 studio
- T2: textura gel/creme se houver asset; senão macro do gloss black + gold type
- Série visual coesa: 4 tubos lado a lado = lineup forte
