# Lançamento paletas out/2026: fotos (STONE · SUNSET)

Run: 07/10/2026 · Magnific · Nano Banana Pro (`imagen-nano-banana-2`) @ 2k · i2i com packshot oficial como identity lock.

- STONE = Vital renomeada, SUNSET = Enérgica renomeada (cliente). Refs: packshots `01` de Vital e Enérgica (Shopify CDN).
- PETAL: **não gerada**, cores desconhecidas (ver ficha). ALLURE/AURA: fora do lançamento.

## Run 1: REPROVADO pelo cliente

Motivo: superfície de mármore/pedra (o cliente quer fundo só preto). Não usar.

### Stills do run 1

| Arquivo sugerido | Formato | Link Magnific |
|------------------|---------|---------------|
| stone-hero-a | 4:5 feed dark | https://www.magnific.com/app/creation/WDQnWdDcXe |
| stone-hero-b | 4:5 feed dark | https://www.magnific.com/app/creation/P3dOP2Q42C |
| sunset-hero-a | 4:5 feed dark | https://www.magnific.com/app/creation/gOcsg3bSXO |
| sunset-hero-b | 4:5 feed dark | https://www.magnific.com/app/creation/lJWLl33gv9 |
| duo-stone-sunset-a | 9:16 story/reels | https://www.magnific.com/app/creation/79MU7TUJAL |
| duo-stone-sunset-b | 9:16 story/reels | https://www.magnific.com/app/creation/Sy0lScXUb8 |

Os PNGs **não estão no repo**: o CDN do Magnific (`pikaso.cdnpk.net`) é bloqueado pela rede do container da sessão. Baixar pelo link acima após o QC (`output/` é ignorado pelo git).

## Gate de QC (still-verifier, antes de qualquer uso)

1. Monograma LF + "LF PRO" gold na tampa, iguais ao packshot (sem letra deformada)
2. **Nenhum texto novo** na tampa (nada de "STONE"/"SUNSET" escrito no compacto)
3. Grade 2×3, 6 pans, espelho na tampa
4. Cores dos pans = Vital (STONE) / Enérgica (SUNSET), na mesma posição
5. Sem rosto, sem texto alucinado

## Prompts

### STONE hero (4:5)
```
Luxury eyeshadow launch hero photograph. Use the reference image as an exact product identity lock: the same LF PRO black square compact eyeshadow palette, reproduced exactly. Composition: the closed compact standing slightly behind on the left showing the large gold LF monogram and "LF PRO" on the lid exactly as in the reference, and the open palette in front on the right, mirror lid up, 6 pans in a 2x3 grid with exactly the reference colors: top row matte black, matte burgundy, matte cool brown; bottom row matte cool grey, matte rose taupe, champagne white shimmer. Do not add any text or product name to the lid. Scene: deep black studio background, polished dark stone surface with a soft reflection, warm gold rim light tracing the compact edges, soft crushed powder of the same six shades scattered at the base. Premium cosmetics campaign, photorealistic, sharp focus on the pans, no extra text, no people.
```

### SUNSET hero (4:5)
Igual ao STONE, trocando os pans por: `top row matte coral terracotta, bronze shimmer, matte rust copper; bottom row soft-shimmer light peach, matte warm brown, matte peach nude`, luz `warm golden sunset-toned rim light` e pó `same six warm shades`.

### Duo STONE + SUNSET (9:16)
```
Luxury eyeshadow launch duo photograph, vertical. Two LF PRO black square compact eyeshadow palettes, each an exact copy of its reference image: reference 1 (cool palette: matte black, matte burgundy, matte cool brown / matte cool grey, matte rose taupe, champagne white shimmer) on the left, reference 2 (warm palette: matte coral terracotta, bronze shimmer, matte rust copper / soft-shimmer light peach, matte warm brown, matte peach nude) on the right. Both open with mirror lids up, standing and leaning toward each other at a slight angle, mirrored symmetry, pans in a 2x3 grid exactly as in the references. Keep pan colors, layout and compact geometry identical to the references; no text or names added to any surface. Scene: deep black studio, dark polished surface, warm gold rim light along the compact edges, subtle crushed powder at the base. Premium cosmetics campaign, photorealistic, no people, no extra text.
```

## Run 2 (uma por vez, fundo preto puro)

Refs: packshot Vital `01` (compacto + textura matte) + packshot Enérgica `01` (textura do cintilante). Cores via hex no prompt, medidas nas refs do cliente.

| # | Paleta | Formato | Link | Status |
|---|--------|---------|------|--------|
| 1 | PETAL | 4:5 | https://www.magnific.com/app/creation/dtreg5QXSL | quase: pans invertidos (ref estava de cabeça p/ baixo) |
| 2 | PETAL v2 | 4:5 | https://www.magnific.com/app/creation/VXbTUu3MMU | ✅ aprovada |
| 3 | BASIC | 4:5 | https://www.magnific.com/app/creation/ovLBirq829 | ✅ aprovada |
| 4 | STONE | 4:5 | https://www.magnific.com/app/creation/N2oNZMW6D9 | aguardando cliente (ref só Vital 01) |
| 5 | SUNSET | 4:5 | https://www.magnific.com/app/creation/UPTUyY9wny | aguardando cliente (ref só Enérgica 01) |

## Série 2: swatch story (uma por paleta)

Estética pedida pelo cliente (ref `assets/refs/paletas/lancamento-sunset-stone-petal/estetica-swatch-story-ref.webp`): 9:16, **fundo preto**, 6 godets soltos em zigue-zague vertical, cada um com o swatch de pó esmagado por trás, **sem texto**. Textura do pó: ref `Paleta_Energica_2.png` (site). Ordem dos godets: topo esq. → base dir. Fazer a primeira, aprovar, e só depois replicar.

| # | Paleta | Link | Status |
|---|--------|------|--------|
| 1 | PETAL | https://www.magnific.com/app/creation/yid9LcMPW9 | ✅ aprovada (modelo da série) |
| 2 | BASIC | https://www.magnific.com/app/creation/yid9lgUPW9 | ❌ reprovada |
| 3 | STONE | https://www.magnific.com/app/creation/UPVJx63wny | ✅ aprovada |
| 4 | SUNSET | https://www.magnific.com/app/creation/79DyjU5JAL | ❌ reprovada |
| 5 | SUNSET v2 (molde = STONE aprovada) | https://www.magnific.com/app/creation/w4MOgOC7EI | ajuste: bronze vinha cintilante |
| 7 | SUNSET v3 (só o pêssego claro cintilante) | https://www.magnific.com/app/creation/N28R2Lr6D9 | ❌ cores divergentes da Enérgica (hex antigos errados) |
| 8 | SUNSET v4 (hex reais da Enérgica 01) | https://www.magnific.com/app/creation/jUngBOJLD0 | aguardando cliente |
| 6 | BASIC v2 (molde = PETAL aprovada) | https://www.magnific.com/app/creation/iGtZ9pZ3uK | ✅ aprovada |

Regra do cliente: SUNSET replica as formas da STONE; BASIC replica as formas da PETAL. Mesmas posições e swatches, só as cores mudam.

## Série 3: cascata com as 4 paletas

Ref de composição (cliente): `assets/refs/paletas/lancamento-sunset-stone-petal/estetica-cascata-4-paletas-ref.png`. Flat lay de cima, 4 paletas abertas em zigue-zague diagonal, **fundo preto**, sem texto. Ordem de cima para baixo: PETAL, BASIC, STONE, SUNSET. Hex da STONE medidos no packshot real da Vital `01.png`: `#0C0A0B #531A19 #693930 / #6C6262 #B27C73 #E5DDDF` (só o último é cintilante).

| # | Link | Status |
|---|------|--------|
| 1 | https://www.magnific.com/app/creation/tCSCV08mZJ | ajuste: muito travado/alinhado |
| 2 | https://www.magnific.com/app/creation/79D9jheJAL | aguardando cliente (posições soltas, cortes na borda, tampas em ângulos diferentes) |
