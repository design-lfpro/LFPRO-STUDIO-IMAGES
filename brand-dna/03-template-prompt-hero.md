---
tags: [lfpro-studio, prompt, nano-banana, template]
status: validado
updated: 2026-11-19
---

# Template de prompt — hero de produto (Nano Banana Pro @ 2k)

Estrutura que entregou **fidelidade de embalagem** (logo LF correto, sem texto inventado) nas sessões de nov/2026.
Imagens aprovadas com esta estrutura: hero Soft Eye + Rose + Base 03, Base + Luminous, story Base + 4 primers (v1),
hero Candy + Blend Cream + Classic + Essential Mauve (v3), Classic Lips Rose com swatch.

## Regras que fazem funcionar

1. **Referências = só packshots oficiais**, 1 por produto, **máximo 4–5 produtos**. Sem imagem de composição
   (referência de composição faz o modelo copiar produtos/estrutura errados).
2. **Composição, câmera e luz descritas em texto**, em blocos com cabeçalho (CAMERA / LIGHT / REAL-WORLD SCALE / PRODUCT FIDELITY).
3. **Medidas reais em cm** de cada item (ver `02-medidas-embalagens.md`) + a relação com o item âncora.
4. **Nunca numerar** a lista de produtos (o modelo imprime "1, 2, 3" nas embalagens).
5. **Não listar todo o texto da embalagem** nem pedir rótulos: descrever "gold monogram exactly as the packshot".
6. Bloco final obrigatório: `never typed-letter logos, never added or garbled text, never write product names on the packaging`.
7. Descrever o acabamento externo quando o modelo erra (ex.: Cream Color = estojo **preto** brilhante, dourado só por dentro).
8. 1 imagem por vez, 2k (75 créditos). 4k = 150.

## Template

```text
Ultra-realistic high-end beauty campaign hero photograph, vertical {4:5|9:16}, LF PRO. {N} products are the heroes,
grouped in the lower {55}% of the image on a seamless deep matte BLACK studio sweep (#0A0A0A, soft gradient falloff,
no horizon line) with a glossy black floor. Top {40}% is clean empty black. NO text, letters or numbers anywhere
except the original printing on the products.

CAMERA: Phase One IQ4, 100mm macro, f/8, camera low at product height +8 cm, tilted down 8°, focus stacked so all
products are tack-sharp, natural perspective, no distortion.
LIGHT: soft key from upper left (large octabox), thin warm golden rim/strip lights behind tracing the edges of the
glossy black packaging so black separates from black, gold elements with real metallic highlights, soft contact
shadows and faint glossy reflections on the black floor, neutral 5200K, rich blacks with detail.

REAL-WORLD SCALE (keep these ratios exactly):
- {Produto} (reference {n}): {medidas cm}, {acabamento}, {aberto/fechado}, {posição}, {detalhe visual}.
- ...

PRODUCT FIDELITY (critical): each package an exact copy of its reference packshot — same shapes, proportions,
finishes, gold foil LF monogram graphic and small gold typography in the same positions; never typed-letter logos,
never added or garbled text, never write product names on the packaging. Minimal, elegant, editorial luxury,
nothing cropped, no extra objects.
```
