---
family: intense-eye
title: Intense Eye
product_type: Lapiseira Retrátil para Olhos
status: dna-v1-scaffold
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
handles:
  - intense-eye-black
  - intense-eye-brown
---

# Intense Eye — DNA de família

Linha de **lapiseira retrátil (twist-up) para olhos** LF PRO. 2 tons: **Black** e **Brown**.

**Produto ainda não encontrado publicado em lfpro.com.br** (não aparece no catálogo/JSON do site) — SKU, preço, URL e claims pendentes de confirmação. Não inventar.

## Origem dos assets

- Fotos oficiais de ecommerce, pasta do Drive do usuário (`INTENSE EYE / FOTO PRODUTO`), arquivos `INTENSE EYE {TOM} PRODUTO.png`
- Publicadas em `assets/products/intense-eye-{black,brown}/01.png`

## Packaging (lock visual) — NUNCA redesenhar

| Elemento | Lock |
|----------|------|
| **Formato** | **Lapiseira retrátil** (twist-up mecânico), corpo cilíndrico fino e longo — **não** é lápis de madeira apontável |
| **Ponta** | Cônica pontiaguda (já estendida no packshot), na cor do pigmento do tom |
| **Rosca/twist** | Friso/rosca visível no terço inferior do corpo (mecanismo de avanço) |
| **Texto** | Vertical gold, uppercase: `INTENSE EYE` |
| **Logo** | Monograma LF gold (ligature) logo abaixo do texto, próximo à base |
| **Cap** | Tampa cilíndrica separada, mesma cor do corpo, com pequeno furo/rebaixo no topo (encaixe tipo "keyhole"), acabamento glossy |
| **Acabamento corpo** | Glossy (brilhante), não fosco |

## Tons — Black, Brown

Packshot oficial isolado por tom, publicado em `assets/products/intense-eye-{tom}/01.png`. Hex por amostragem de pixel do corpo:

| Tom | Hex aprox. (corpo) | Leitura visual |
|-----|---------------------|-----------------|
| **Black** | `#0A0A0A` | preto glossy profundo |
| **Brown** | `#3B281F` | marrom espresso escuro quente |

- Texto/monograma gold em ambos os tons: `#C9A227` / `#D4AF37` (padrão de marca)
- Hex são aproximados (amostra de still, não de fórmula) — mesma ressalva usada nos demais produtos do catálogo
- Fundo packshot: off-white `#F7F5F2`–`#FAFAF8`

## Textura

- Ponta pigmentada sólida/cremosa (delineador em bastão), cor igual ao corpo do lápis
- Sem swatch macro disponível ainda

## Claims (site — sem inventar)

- Nenhum claim oficial disponível ainda (produto sem página publicada / não localizado no catálogo)

## Prompt anchors (EN) — família

```
LF PRO Intense Eye retractable eye pencil identity lock: slim cylindrical twist-up mechanical pencil, glossy [BLACK|BROWN] casing, gold foil vertical text "INTENSE EYE", gold LF ligature monogram below the text near the base, visible twist/advance mechanism ridge in the lower third, sharp conical pigmented tip already extended, matching-color glossy cap resting separately beside the pencil with a small keyhole-shaped recess on top, seamless off-white #F7F5F2 background, soft studio light, photorealistic ecommerce product photo, exact shape and logo, no redesign, not a wood pencil.
```

## Anti-patterns

- Redesenhar formato da lapiseira, cor do corpo ou lettering
- Tratar como lápis de madeira apontável (é retrátil/twist-up)
- Trocar hex entre tons (Black ≠ Brown)
- Inventar SKU, preço, URL ou claims
- Logo prata/branco ou monograma inventado
- Full-face / eye-proof V1 (T5 bloqueado)

## Notas V1

- 2 assets publicados (`01.png` por tom), origem Drive `FOTO PRODUTO`
- Pendências: SKU, preço, URL, claims oficiais, swatch/textura macro

## Retrato com modelo (T4 antecipado a pedido do cliente)

Personagens cadastradas no Magnific: `intense-eye-modelo-black` (tom Black) e `intense-eye-modelo-brown` (tom Brown). Nunca misturar modelo e tom.

| Regra | Detalhe |
|-------|---------|
| **Cor por tom** | Fundo, roupa, unha e make **sempre** na cor do produto: Black = preto · Brown = marrom |
| **Roupa** | **Exatamente a da foto de personagem** — não descrever/inventar peça nova no prompt |
| **Escala** | Lapiseira **fina e delicada** (~13 cm, mais fina que um dedo) — nunca maior que a mão/rosto |
| **Ponta** | Igual ao packshot `01.png` — não inventar ponta de caneta feltro nem cone longo/agulha |
| **Geração** | **1 imagem por vez** (`count: 1`) |
| **Pose de referência** | Descrever em texto; não subir imagem com produto/marca de terceiros |
| **Ponto de contato** | Ponta da lapiseira **na linha dos cílios / delineado do olho** — nunca na sobrancelha (é produto de olho, não de sobrancelha) |

Feedback 2026-09-30 (reprovado): roupa diferente da personagem, produto grande demais na mão, ponta diferente da real.

Feedback 2026-09-30 (pose close brown, mão pela direita, mindinho na bochecha): fidelidade de pose **aprovada**; erro = ponta posicionada na cauda da sobrancelha em vez do delineado. Na próxima: "pencil tip touching the upper lash line at the outer corner of the eye, drawing the eyeliner".

### Anatomia real (lida do packshot `01.png`) — usar em todo prompt de produto

1. ~55% inferior: corpo cilíndrico reto glossy, texto `INTENSE EYE` gold vertical + monograma LF (glifo fluido tipo fita, **nunca** letras "LF" legíveis)
2. Colar com **dois anéis finos** em relevo onde o corpo termina
3. Acima do colar: luva levemente mais fina, mesma cor, afinando **muito gradualmente** no terço superior
4. Na ponta: só **alguns milímetros** de pigmento, mesma cor — **não** grafite longo exposto, **não** agulha
5. Tampa: cilindro liso glossy, topo arredondado com furinho, ~1/3 do comprimento

Feedback 2026-10-01 (flat lay 2 cores, luz diagonal): reprovado — embalagem e **ponta** erradas, saiu uma **3ª lapiseira**, monograma virou "LF" legível. Correção: usar packshots como referência `image` direta (uploads `INTENSE EYE BLACK/BROWN PRODUTO.png` no Magnific) além da ficha de produto, travar contagem ("EXACTLY FOUR OBJECTS") e descrever a anatomia acima.

Feedback 2026-10-01 (duas modelos sorrindo, olhando o horizonte): reprovado — **identidade das modelos perdida** (saíram outras pessoas). Causa provável: só refs de personagem da biblioteca + 2 refs de produto diluindo. Correção: passar as **fotos originais das modelos** como referência `image` direta (uploads no Magnific: black = loira, blazer preto, fundo preto, mão no queixo; brown = cabelo castanho preso, blazer marrom, colar dourado, fundo marrom) + bloco "IDENTITY LOCK" no prompt, e omitir produto quando não for necessário.
