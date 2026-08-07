---
handle: pincel-para-base-f01
title: Pincel para Base F01
family: pinceis
product_type: Pincel
url: https://lfpro.com.br/products/pincel-para-base-f01
sku: "12667"
price: "89.90"
preferred_tracks:
  - T1-product-hero
  - T3-tools-hands
blocked_tracks:
  - T5-face-proof
status: ready
assets_local: assets/products/pincel-para-base-f01/
---

# Pincel para Base F01

Pincel de construção de pele. Cabeça **angular crescente** densa + cabo preto + logo gold `F01`. Tool hero da linha — aparece solo, em trio e em uso com base líquida.

---

## Identidade

| Campo | Valor |
|-------|-------|
| Código | **F01** |
| Função | Aplicação de base (líquida/creme); construção de cobertura |
| Silhueta | Cabeça diagonal larga + pescoço cônico gloss + cabo cilíndrico |
| Diferencial de forma | **Formato angular crescente** — acompanha nariz, sub-olho, maxilar |
| Persona visual | Pro, preciso, “performance tool” (não fluffy blush brush) |

---

## Packaging / objeto lock

### Forma da cabeça (crítico)

- Vista frontal packshot: cabeça em **meia-lua diagonal / slanted kabuki**.
- Borda superior **inclinada** (mais alta em um lado, mais baixa no outro) — ângulo crescente.
- Largura da cabeça maior que o diâmetro do cabo; fan denso, não sparse.
- Em perfil (uso na bochecha): face da cerda plana-convexa; se encaixa na maçã do rosto e laterais do nariz.
- **Não** é dome redondo (isso é C02). **Não** é flat top 100% reta.

### Cerdas

- **Ombré dual-tone:** pontas brancas/cinza-claras (`#F2F2F2`) → base preta densa no ferrule (`#1A1A1A`).
- Empacotamento muito denso; em macro (asset `03`) fibras individuais legíveis, brilho suave na ponta.
- Duplo polimento: superfície “lustrosa” quando molhada com base (asset `03` — base bege escorrendo na face angular).
- Altura da cerda: média-alta; proporção cabeça ~1/4–1/3 do comprimento total do pincel.

### Ferrule / pescoço

- Preto **high-gloss**.
- Forma **cônica alargada** sob a cabeça (flared neck) — signature F01.
- Transição suave do gloss do pescoço para o corpo fosco do cabo (linha de junção visível).

### Cabo

- Cilíndrico, preto profundo, acabamento semi-matte.
- Extremidade inferior **arredondada** (bullet).
- Comprimento generoso para grip completo (mão segura no terço inferior — asset `08`).

### Gravação LF PRO

- Vertical no cabo, dourado foil:
  1. Monograma **LF** (geométrico)
  2. `/`
  3. Wordmark **LF PRO**
  4. Código **F01** próximo à ponta inferior
- Em flatlay (asset `09`): logo legível nas duas orientações (cabeça cima / cabeça baixo).

---

## Cores hex

| Elemento | Hex |
|----------|-----|
| Cabo deep black | `#0A0A0A` |
| Ferrule gloss | `#1C1C1C` + specular `#FFFFFF` soft |
| Cerda tip | `#F0F0F0` / `#E6E6E6` |
| Cerda base | `#121212` / `#252525` |
| Logo gold | `#C9A84C` / `#D4AF37` |
| Fundo packshot | `#F7F5F2` |
| Base líquida (ref uso) | `#C4A07A`–`#A67C52` (beige médio; não fixar shade) |

---

## Logo

- Gold foil, vertical, contraste alto no cabo preto.
- Monograma LF + `LF PRO` + `F01` — **nunca omitir o código F01** em stills hero se o packshot o mostra.
- Escala: pequena e nítida; se ilegível no frame, o output falhou o lock.

---

## Textura

- Cerdas plush-densas; quando com produto, a base **assenta e escorre levemente** nas pontas (baixa absorção).
- Cabo: micro-textura matte; ferrule: espelho com catch-lights alongados.
- Em dark studio: highlight quente no gloss do pescoço + bokeh circular (asset `08`).

---

## Foto estúdio (mapa de assets)

| File | Conteúdo | Uso |
|------|----------|-----|
| `01.png` | Packshot isolado off-white, cabeça angular up | **T1 identity lock** |
| `02.png` | Macro aplicação na maçã do rosto (rosto full) | âncora humana — não gerar T5 |
| `03.png` | Macro cerdas + pump gold + base pingando | T1/T3 texture + product load |
| `07.png` | Modelo aplicando na bochecha, camarim | âncora pose (rosto full = ref only) |
| `08.png` | Mão segura o pincel vertical, dark + gold bokeh | **T3 gold** |
| `09.png` | Duo flatlay em bandeja preta (duas orientações) | T1 composition |

---

## Prompt anchors EN

### Still — identity lock

```text
LF PRO F01 foundation brush, exact angular crescent dense brush head slanted on one side,
synthetic dual-tone bristles soft white tips fading to dense black base at ferrule,
high-gloss black flared conical neck, matte black cylindrical handle with rounded tip,
vertical gold foil monogram LF and wordmark "LF PRO" and code "F01" engraved on handle,
premium beauty ecommerce product photo, seamless off-white background #F7F5F2,
soft drop shadow, sharp bristle fibers, no wood, no rose gold, no round dome head
```

### T1 hero — dark-feed

```text
LF PRO F01 black foundation brush floating on pure black background, warm gold rim light,
specular highlights on glossy black ferrule, dual-tone white-to-black bristles clearly visible,
angular slanted brush head silhouette, gold logo readable, luxury beauty commercial still,
shallow depth of field, cinematic product photography
```

### T1 hero — product load (optional beat)

```text
extreme close-up of LF PRO F01 angular brush head, liquid foundation beige cream pooling
on dense dual-tone bristles, soft drip from white tips, high-gloss black ferrule in frame,
black background, luxury beauty macro, razor-sharp fiber detail, no full face
```

### T3 hands-in-use (SEM rosto full)

```text
elegant medium-brown skin hand with natural nude manicure holding LF PRO F01 foundation brush
vertically, only hand wrist and tool visible, dark studio background with warm circular bokeh,
matte black handle gold "LF PRO" and "F01" engraving readable, angular dual-tone bristle head,
beauty commercial lighting, no face, no portrait, no full makeup application on face
```

```text
close crop: fingertips gripping matte black F01 handle, brush head out of focus soft,
or brush head sharp and hand secondary, never full face in frame
```

---

## Anti-patterns

- Cabeça **redonda/dome** (confundir com C02)
- Flat-top 90° sem ângulo crescente
- Cerdas monocor pretas ou só brancas
- Cabo curto stubby / cabo dourado / ferrule prata
- Logo sem `F01` ou monograma inventado
- Gerar aplicação full-face / skin finish proof (T5)
- Inventar “cerdas naturais de cabra” ou claims fora do site

---

## Claims site

Fonte: `body_text` Shopify.

- Aplicação **rápida**, acabamento profissional, máxima eficiência de produto.
- Design técnico facilita espalhabilidade com **mais controle**; cobertura construível, natural e sofisticada.
- **Formato angular crescente** acompanha contornos do rosto (laterais do nariz, abaixo dos olhos, linha do maxilar) → precisão + acabamento uniforme.
- Cerdas com **duplo polimento**: espalham e refinam ao mesmo tempo → menos marcas.
- **Densidade calibrada** reduz absorção excessiva → melhor rendimento da base, aplicação mais rápida.

---

## Notas V1

- Packshot `01.png` = verdade de silhueta. Qualquer still deve passar no teste “é o F01 angular, não um kabuki genérico”.
- T3 preferir pose de asset `08` (mão + tool dark) em vez de clonar `02`/`07` (full face).
- Excelente par visual com **Base Soft Matte** (pump gold no asset `03`) — cross-product T3 permitido se F01 continuar lockado.
- Parte do [[trio-pinceis]]; em kit, manter cabeça angular distinguível de C02 e B03.
