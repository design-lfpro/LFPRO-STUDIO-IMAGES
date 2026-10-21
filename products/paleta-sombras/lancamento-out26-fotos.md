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
| 2 | https://www.magnific.com/app/creation/79D9jheJAL | composição ✅, produto ❌ (STONE saiu 3×3 com 9 godets, BASIC deformada) |
| 3 | https://www.magnific.com/app/creation/mEUEo9UhJQ | ❌ não mudou (molde herdou a deformação) |
| 4 | https://www.magnific.com/app/creation/fHOqEE5CDY | composição ok, ❌ divisões entre godets grossas |
| 5 | https://www.magnific.com/app/creation/SyTPOlyUb8 | substituída pela v6 |
| 6 | https://www.magnific.com/app/creation/EbP51wLuuO | formato/composição ✅, ❌ espelho com degradê branco CGI |
| 7 | https://www.magnific.com/app/creation/KLZsP6tkqp | aguardando cliente (molde v6 + espelho escuro real + linguagem ultrarrealista) |

Geometria real medida no packshot: divisória ≈ 1/10 da largura do godet; godets ocupam ≈ 90% da base; aro externo fino.

Anti-pattern recorrente em cenas com várias paletas: o modelo inventa grade 3×3 / compacto quadrado. Sempre reforçar **6 godets 2×3, base retangular horizontal, dobradiça no lado maior**.

## Correção PETAL: 3 cintilantes (08/10/2026)

O cliente enviou uma amostra de fábrica mostrando que o rosa terracota (base esq.) também é cintilante. Fotos aprovadas refeitas usando a própria foto como molde e mudando só esse acabamento:

| Foto | Link | Status |
|------|------|--------|
| PETAL hero 4:5 (molde: PETAL v2) | https://www.magnific.com/app/creation/YMQE7GyWeC | ok, mas topo dir. pink demais |
| PETAL hero 4:5 v2 (topo dir. rosa coral #D88080) | https://www.magnific.com/app/creation/gO00mzCSXO | ⚠️ coral descartado: refazer com cores da foto oficial de 08/10 |
| PETAL swatch story 9:16 (molde: swatch v1) | https://www.magnific.com/app/creation/lJcYCS1gv9 | ok, mas tom 3 pink demais |
| PETAL swatch story 9:16 v2 (tom 3 rosa coral #D88080) | https://www.magnific.com/app/creation/SyTThVWUb8 | ⚠️ coral descartado: refazer com cores da foto oficial de 08/10 |
| Cascata 4 paletas | (pendente: refazer quando a v7 for aprovada) | |

Elemento `LFPRO-Paleta-PETAL` (2366895) atualizado em 08/10 com a foto oficial corrigida e os hex medidos nela.

## Correção BASIC: 2 cintilantes (14/10/2026)

O tom mais claro (pêssego nude, base dir.) também é cintilante. Foto principal (`01 BASIC`, foto oficial do site) retocada **só no godet base dir.**, com máscara `assets/refs/paletas/masks/basic-01-mask-base-dir.png` (x 739–841, y 610–686) e retouch Nano Banana Pro. O resto da foto não muda.

| Foto | Link | Status |
|------|------|--------|
| 01 BASIC retocada (base dir. cintilante) | https://www.magnific.com/app/creation/ovglYnp829 | ❌ ficou igual (retoque IA sutil demais) |
| 01 BASIC retoque local (textura do rosé cobre + cor real) | `assets/products/paleta-de-sombras-basic/01.png` | ✅ aprovada; elemento 2390994 atualizado (imagem + descrição) |

## Refação com as cores definitivas (15/10/2026)

Fonte de cor: fotos oficiais de 14/10 (`assets/products/{handle}/01.png`) + elementos novos (PETAL 2390993, BASIC 2390994). Molde de composição: a própria imagem aprovada antes.

| Imagem | Molde | Link | Status |
|--------|-------|------|--------|
| PETAL foto do produto 4:5 | PETAL v2 aprovada | https://www.magnific.com/app/creation/79eC6pIJAL | aguardando cliente |
| BASIC foto do produto 4:5 | BASIC aprovada | https://www.magnific.com/app/creation/lJTmyDNgv9 | aguardando cliente |
| PETAL swatch story 9:16 | PETAL swatch v1 aprovada | https://www.magnific.com/app/creation/bxZDLYS5Y2 | aguardando cliente |
| BASIC swatch story 9:16 | BASIC swatch v2 aprovada | https://www.magnific.com/app/creation/s70tOBEl8e | aguardando cliente |

Sem refação: STONE swatch (cores corretas). SUNSET e cascata ainda não aprovadas.

## 4 paletas fundo branco (refação com cores definitivas, 15/10/2026)

Molde: imagem aprovada do cliente (`assets/refs/paletas/lancamento-sunset-stone-petal/composicao-4-paletas-fundo-branco.png`), com cores antigas. Refeita com as mesmas posições e rotações + os 4 elementos de 14/10. Cores mapeadas por posição visual, considerando a rotação de cada paleta (dobradiça = fileira 1).

| Imagem | Link | Status |
|--------|------|--------|
| 4 paletas fundo branco 3:4 | https://www.magnific.com/app/creation/jUW8tfALD0 | aguardando cliente |

## Série modelo, olhar em destaque (15/10/2026)

⚠️ Exceção aprovada pelo cliente à regra V1 "sem prova de maquiagem no rosto" (T5). Modelos cadastradas pelo cliente no Magnific: stone-modelo 2393752 · petal-modelo 2393753 · basic-modelo 2393755 · sunset-modelo 2393748.
Regras: fundo sempre preto; 4:5; maquiagem dos olhos SÓ com os tons da paleta (nunca copiar a maquiagem das fotos de inspiração); boca/blush neutros; sem produto no quadro; uma por vez.
Poses (inspiração do cliente, descritas em texto, fotos de terceiros não salvas): STONE = mãos emoldurando o rosto, olhar direto · PETAL = cabeça inclinada apoiada nas mãos, olhar para cima/lado · BASIC = mão sob o queixo, ¾ · SUNSET = por cima do ombro, perfil ¾.

| Paleta | Link | Status |
|--------|------|--------|
| STONE v1 4:5 | https://www.magnific.com/app/creation/ksGXCVo16B | ❌ unhas nude (original é preta), sem roupa/acessórios |
| STONE v2 9:16 | https://www.magnific.com/app/creation/mE7GawYhJQ | ajuste: olhar pouco imponente |
| PETAL 9:16 (cabeça inclinada nas mãos) | https://www.magnific.com/app/creation/6AmkYEziJO | ajuste: olhar pouco imponente |
| PETAL v2 9:16 (¾, queixo baixo, olhar firme, dedos na maçã do rosto) | https://www.magnific.com/app/creation/tCwAKLZmZJ | ❌ igual à foto original |
| PETAL v3 9:16 (mão na testa/linha do cabelo, antebraço cruzado, frontal, close) | https://www.magnific.com/app/creation/Cq4cRySEEy | aguardando cliente |
| STONE v3 9:16 (¾, queixo baixo, olhar firme, dedos no maxilar) | https://www.magnific.com/app/creation/iGh1Mpo3uK | ❌ igual à foto original |
| STONE v4 9:16 (câmera baixa, queixo erguido, rosto apoiado na palma, olhar para baixo, close) | https://www.magnific.com/app/creation/iGh1uQB3uK | aguardando cliente |
| BASIC 9:16 (mão sob o queixo) | https://www.magnific.com/app/creation/79eu3vFJAL | ✅ aprovada |
| SUNSET 9:16 (por cima do ombro) | https://www.magnific.com/app/creation/nVFSeUQYQD | ✅ aprovada |

### Regras da série modelo (cliente, 15/10/2026)

- **Só a pose muda.** ID, maquiagem, cabelo, roupa (tomara que caia preto), acessórios (brincos e colar dourados) e mãos (unha preta amendoada com brilho) iguais às fotos originais das modelos, salvo pedido explícito de outro look.
- **Formato padrão: 9:16** (stories; mesmo custo que 4:5).
- Associação modelo ↔ paleta (pelas fotos originais): BASIC = cacheada, esfumado marrom · PETAL = cabelo curtinho, maquiagem rosada · STONE = chanel preto, olhos verdes · SUNSET = ondulado com mechas, maquiagem acobreada.

### Custo por geração via MCP (15/10/2026)

Unlimited do Premium+ **não se aplica** a gerações via MCP (`unlimitedAppliesHere: false`). Por imagem 9:16 com 1 referência:
Nano Banana Pro 2k = 75 · Nano Banana 2 Flash 2k = 75 · Nano Banana 2 Lite = 60 · Seedream 5 Pro 2k = 100 · Nano Banana Pro 4k = 150.
Decisão: manter Nano Banana Pro 2k (mesmo preço do Flash, mais fiel). Para muitas variações, considerar fluxo híbrido (prompt daqui, geração no app com ilimitado).

Padrão de atitude aprovado (BASIC/SUNSET): rosto ¾, queixo levemente baixo, olhar firme direto na lente, sem sorriso.

Lição: com character ref, pose "parecida" com a foto original reproduz a foto. Para mudar de verdade, descrever pose bem diferente + crop mais fechado + "do NOT reproduce the reference pose".

## Série hero por paleta (15/10/2026)

Uma por vez; cada paleta com pose/ângulo diferente; pode ter mais de uma unidade, sempre da mesma paleta; aberta e/ou fechada; fundo preto; 9:16; refs = elemento + foto oficial.

| Paleta | Composição | Link | Status |
|--------|------------|------|--------|
| PETAL | câmera baixa ~15°; 1 aberta em pé inclinada (¾) + 1 fechada deitada mostrando o LF | https://www.magnific.com/app/creation/O6XxtMSynm | ✅ aprovada |
| BASIC v1 | vista de cima; 3 em leque | https://www.magnific.com/app/creation/JNdrErtOq4 | ❌ fundo branco (herdado da foto oficial off-white) + logo LF duplicado/deformado + só 2 unidades |
| BASIC v2 | vista de cima; 1 aberta + 1 fechada | https://www.magnific.com/app/creation/nVF9OSAYQD | ❌ IA deformou (godets 1×6, logo trocado) |
| BASIC v3 (PRODUTO TRAVADO) | composição local: recorte real da `01.png` × 2 (escala/rotação/brilho diferentes), sombra, reflexo, rim | entregue como arquivo (sem custo de créditos) | aguardando cliente |

Lição: NUNCA usar a foto oficial off-white como referência em cena de fundo preto (o modelo copia o fundo). Usar a versão aprovada em fundo preto + elemento. Evitar 3+ unidades sobrepostas (deforma logo/compacto).

### Trava de produto (15/10/2026): composição a partir do packshot real

A IA deforma o compacto em cenas novas. Método travado: `tools/product_cutout.py` recorta a foto oficial `01.png` (remove fundo off-white, erode 4px e limpa a borda para não ficar halo) e `tools/product_compose.py` monta a cena 9:16 em fundo preto (posição, escala, rotação, brilho por camada, sombra de contato, reflexo na superfície, rim light sutil). O produto é pixel a pixel o real: formato, godets, cores e logo não variam. Limite: só rotação no plano/escala (a foto é frontal), sem ângulos 3D novos.

### BASIC: pilha em leque (ref. de composição do cliente, descrita em texto; 19/10/2026)

Ângulo 3D (não dá para fazer por composição local) → IA com trava: ref = BASIC fundo preto aprovada + elemento; 2 fechadas empilhadas giradas + 1 aberta no topo; câmera ~50°.

| Imagem | Link | Status |
|--------|------|--------|
| BASIC pilha em leque 9:16 | https://www.magnific.com/app/creation/O6BjKxRynm | ✅ produto ok; ❌ fundo preto chapado |
| BASIC pilha em leque v2 (estúdio preto ambientado) | https://www.magnific.com/app/creation/O6BjO1synm | aguardando cliente |

Regra de ambiente (cliente, 19/10/2026): fundo preto **ambientado**, nunca preto chapado: sweep preto/grafite com gradiente de luz, superfície acrílica preta com reflexo real, sombras de contato, rim light. Linguagem ultrarrealista.

### PETAL + BASIC lado a lado com pó esmagado (ref. de composição do cliente, descrita em texto; 19/10/2026)

Paletas giradas em retrato (3×2), espelhos abertos para fora (PETAL à esq., BASIC à dir.), pó esmagado dos tons de cada uma em volta; estúdio preto ambientado. Cores mapeadas por posição considerando a rotação.

| Imagem | Link | Status |
|--------|------|--------|
| PETAL + BASIC pó esmagado 9:16 | https://www.magnific.com/app/creation/cp5RM240eP | aguardando cliente |

### PETAL + BASIC lado a lado com pó triturado — v2 PRODUTO TRAVADO (19/10)
- v1 IA (cp5RM240eP) **reprovada: produto deformado**.
- v2: composição local com os recortes REAIS das fotos do site (`tools/product_compose.py`, camadas com `"cut"`), PETAL em cima / BASIC embaixo, 9:16. Base: `assets/refs/paletas/lancamento-sunset-stone-petal/lock/petal-basic-lock-v1.png`.
- IA só no fundo: retouch *precise* com máscara (produto + margem 12px protegidos) → estúdio preto ambientado + pó triturado nos tons de cada paleta. https://www.magnific.com/app/creation/yiogZZqPW9 (75 cr). Status: aguardando aprovação.
- Limite: o produto fica no ângulo frontal da foto do site (sem novos ângulos 3D). Para ângulos novos sem deformar → fotos reais do produto nesse ângulo.

### PETAL torre empilhada + aberta em pé (ref. de composição do cliente descrita em texto; 19/10)
- 3 PETAL fechadas empilhadas em leque solto, a de baixo saindo da borda de um plinto preto brilhante; 1 PETAL aberta em pé no topo (dobradiça vertical à esquerda, espelho aberto como livro, pans 3×2 por causa da rotação). Estúdio preto ambientado.
- Trava de embalagem no prompt + refs: imagem aprovada PETAL fundo preto, foto oficial 14/10, elemento PETAL.
- https://www.magnific.com/app/creation/yioSjVzPW9 (Nano Banana Pro 2k, 9:16, 75 cr). Status: aguardando cliente.
- Risco: ângulo 3D novo + vários produtos → conferir divisórias, grid 2×3, logo único e cores.

### 4 paletas — torre (ref. still-life de potes empilhados, descrita em texto; 19/10)
- Geração única com bloco fixo `prompt-trava-produto.md`. 2 fechadas empilhadas (pedestal) + SUNSET aberta no topo, PETAL encostada à esq. num disco preto, STONE deitada à frente-dir. com esfera de vidro, BASIC em pé atrás à dir.
- https://www.magnific.com/app/creation/lJVr40ngv9 (Nano Banana Pro 2k, 9:16, 75 cr). Status: aguardando cliente.
- v1 (lJVr40ngv9): posição aprovada, **produtos errados** (10–12 pans, rótulos). Causa: 8 refs, incluindo imagens de swatch.
- v2: só os 4 elementos de produto como ref; prompt reforça "EXACTLY SIX pans 2x3, never 8/10/12, no labels". https://www.magnific.com/app/creation/eILTCy4dqL (75 cr). Status: aguardando cliente.
- Lição: em cenas com várias paletas, usar **apenas os elementos de produto** como ref; nada de imagens de swatch/composição.

### STONE aberta + cartucho em pé atrás (ref. de composição palette+box, descrita em texto; 21/10)
- Refs (só 2): elemento STONE 2390996 + painel frontal do cartucho recortado da arte (`lock/stone-cartucho-painel-frontal.png`, sem linhas de faca/código de barras).
- Paleta aberta em 3/4 no primeiro plano, cartucho STONE em pé atrás à direita. Estúdio preto ambientado.
- https://www.magnific.com/app/creation/mEOic1YhJQ (Nano Banana Pro 2k, 9:16, 75 cr). Status: aguardando cliente.
- v2 (cliente: trocar cartucho por paleta fechada + fundo mais preto): ref = v1 mEOic1YhJQ + elemento STONE. Cartucho → STONE fechada em pé (só monograma LF + "LF PRO" na tampa); fundo quase preto com gradiente bem sutil. https://www.magnific.com/app/creation/LwTXQNpswO (75 cr). Status: aguardando cliente.
- v2 feedback: fechada saiu **quadrada**; fundo pode ser ainda mais preto.
- v3: https://www.magnific.com/app/creation/p8L7Wtlehw (75 cr) — prompt pediu retângulo ~1,7:1. **Atenção:** medição posterior no packshot oficial (`assets/products/paleta-de-sombras-stone/01.png`): tampa fechada ≈ 415×330 px → **≈1,25:1** (levemente retangular, fina). Se v3 saiu alongada demais, refazer com 1,25:1.

### SUNSET fechada em pé + aberta atrás, feixe de luz (ref. de composição palette duo, descrita em texto; 21/10)
- Ref: só elemento SUNSET 2390997. Fechada em pé no primeiro plano à esq., aberta atrás à dir.; fundo preto + feixe de luz quente de janela cruzando a cena.
- https://www.magnific.com/app/creation/If7NMDBtvE (75 cr). Status: aguardando cliente.

### Fechada TRAVADA (21/10) — STONE v4 e SUNSET v2
Cliente: fechadas deformadas em STONE v3 e SUNSET v1 (IA inventa logo LF serifado e proporção). SUNSET: sem tecido, superfície lisa, luz menos focada, reflexo integrado (espelho mostrava parede branca).
Método: (1) `tools/lid_texture.py` reconstrói a tampa fechada REAL do packshot oficial (logo/wordmark = pixels reais; ~1/3 direito oculto completado espelhando a borda lisa) → `assets/refs/paletas/lancamento-sunset-stone-petal/lock/lid-fechada-real.png` (424×327, ≈1,3:1). (2) `tools/closed_lid_place.py` apaga a fechada falsa (interpolação do fundo) e aplica a tampa real em perspectiva com espessura, rim light, sombra de contato e reflexo.
- STONE v4 = STONE v3 (p8L7Wtlehw) com fechada apagada + tampa real → `entregas/lancamento-out26/stone-aberta-fechada-v4.png`
- SUNSET v2: cena IA só com a aberta (Td1SDNPVNR, 75 cr; superfície acrílica preta lisa, luz difusa, espelho escuro) + tampa real no primeiro plano à esq. → `entregas/lancamento-out26/sunset-aberta-fechada-v2.png`
- Regra nova: **fechada nunca por IA** — sempre tampa real aplicada localmente.

### Refeitas DO ZERO no Magnific com trava de prompt (cliente, 21/10)
Cliente: montagem local (STONE v4 / SUNSET v2) ficou fora do padrão, não realista → refazer 100% no Magnific. Passe de realismo intermediário (SUNSET ksn8CMI16B, STONE MBx9Gg2DCm) descartado pelo pedido.
Refs (só 2): elemento da paleta + tampa fechada real (`lock/lid-fechada-real.png`, upload 9ZmkUM3NYZ). Trava: proporção ≈1,3:1, espessura ≈1/12 da largura, monograma LF sans fino + "LF PRO", 6 pans 2×3 com hex.
- Rodada 1 (9ZmkUfDNYZ SUNSET, jU0hqmjLD0 STONE): fechada saiu em RETRATO (em pé no lado curto); STONE com logo de lado. Reprovadas internamente.
- Rodada 2 (+ "LANDSCAPE: visible face wider than tall, logo upright, stands on LONG edge"):
  - SUNSET v4 https://www.magnific.com/app/creation/lJMfklQgv9 — fechada horizontal, logo correto, reflexo integrado. Status: aguardando cliente.
  - STONE v5 https://www.magnific.com/app/creation/rgWtqlpxtc — fechada horizontal, logo de pé; tampa brilhante reflete a paleta (pode parecer "pans" na tampa). Status: aguardando cliente.
- Lição: para fechada em pé, sempre escrever "stands on its LONG edge, landscape, wider than tall, logo upright" e mandar a tampa real como ref.

### PETAL + BASIC flat lay com pó triturado (ref. editorial de 2 paletas abertas em retrato, descrita em texto; 21/10)
Refs: só elementos PETAL 2390993 + BASIC 2390994 (+ geração anterior como base nas iterações). Cores mapeadas por posição com rotação (PETAL dobradiça à esq.: col. esq. 8F4148/AF8981✦/E5B5A5✦, col. dir. A36869/5E2D40/9B5B55✦; BASIC dobradiça à dir.: col. esq. C99167/AE7460✦/E6B19C✦, col. dir. 714A3D/9D614A/AC7E5D).
- v1 s7Vfyvkl8e: cores ✔; pans retangulares, espelhos cortados, composição rígida.
- v2 SypuNsmUb8: composição solta + pó abundante ✔, pans quadrados ✔; estojo arredondado tipo "almofada" ✘.
- v3 https://www.magnific.com/app/creation/ovUAQhv829 — estojo retangular fino com cantos justos ✔, pans quadrados ✔, cores ✔, composição da v2. Pontos: espelhos claros (refletem luz) e encostados na borda. Status: aguardando cliente. (3 × 75 cr)
- Lição: para estojo, escrever "CRISP THIN FLAT RECTANGLE, small tight corner radius, narrow bezel, never pillow-shaped" + "perfectly SQUARE pans".
- PETAL+BASIC v4 XmgZLoPBfo (espelhos): escuros ✔, mas refletem os pans nítidos (parecem paletas extras) e ainda encostam na borda. Aguardando escolha da cliente (espelho levantado ~100° recomendado).

### SUNSET + STONE flat lay (mesma composição; 21/10)
Base de composição ovUAQhv829 + elementos SUNSET 2390997 e STONE 2390996. Mapeamento: SUNSET (dobradiça esq.) col. esq. AF5948/7F4636/C75E57, col. dir. DCA28F/BB7054/E5B2A0✦; STONE (dobradiça dir.) col. esq. 726565/B17B76/E5D9DC✦, col. dir. 100E10/551D20/6B3D37.
- v1 https://www.magnific.com/app/creation/N2hrvmH6D9 — cores ✔, estojo ✔, pó ✔; espelhos claros e encostando nas bordas (herdado da base). Status: aguardando cliente.
- v2 (ref de composição da cliente ksnIotx16B — foto original, usada só p/ composição) https://www.magnific.com/app/creation/P3IK5kz42C — tampas levantadas (~100°) vistas de cima como faixa preta fina, sem espelho branco ✔; cores ✔; pans quadrados ✔; estojo ✔. Pontos: tampas encostam nas bordas laterais; inclinação menor que na ref. Status: aguardando cliente.
