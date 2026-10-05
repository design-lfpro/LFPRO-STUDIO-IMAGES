# Hero Intense Eye — Black & Brown (layout 9:16 "BLACK & BROWN")

- `layout.json` + `v1-composite.png`: base com os pixels reais dos packshots (0 créditos), posicionada pelo rascunho do designer
- Composite no Magnific: creation `vQwq1x8a47`; packshots: black `ovLCQMs829`, brown `dtrvCMbXSL`

## Passada IA v1 (2026-10-05)

- Modelo: `imagen-nano-banana-2` @ 2k, 9:16, count 1 (75 cr)
- Referências: @img1 composite (layout + produto), @img2 packshot black, @img3 packshot brown
- Prompt: "re-render @img1" com a ordem de não mover nem adicionar nada + PRODUCT LOCK (twist-up, colar com 3 anéis, tampa lisa sem logo, só "INTENSE EYE" + monograma LF gold, hex por tom) + mudar só luz/material
- Resultado: https://www.magnific.com/app/creation/UPTNZ1fwny (aguardando revisão)
- Se o lettering ou o logo derivarem: recolar a região do lettering a partir do composite (pixels reais), sem gerar de novo

### Feedback v1 — reprovado
A passada "re-render @img1" foi ignorada pelo modelo: as lapiseiras viraram um X e apareceram texto "INTENSE EYE" gigante e serifado, "LF" literal inventado e tampa cortada.
Lição: a geração com referência (Nano Banana) **não preserva pixels**, então a base composite é tratada só como inspiração.

## Passada IA v2 — do zero, trava no prompt (2026-10-05)
- Refs: só os packshots (@img1 black, @img2 brown); a base composite ficou de fora
- O prompt define a composição em % do quadro (ponta, ângulo, saída pela borda, zonas vazias para texto e logo) e trava o lettering: sans-serif fino e pequeno, altura de ~1/3 da largura do corpo, monograma do tamanho de 1 letra, tampas sem texto. O negativo proíbe X, cruzamento, serif e "LF" literal.
- Resultado: https://www.magnific.com/app/creation/ksZS6jy16B (aguardando revisão)

## v3 — montagem do designer + Upscale criativo (2026-10-05)
- Base: `v2-ref-designer.png`, montagem do designer com os produtos reais e swatches (Magnific `Eby1ipPuuO`)
- Ferramenta: `images_upscale` (mode creative, 2x, preset ThreeDRenders, creativity 3, resemblance 7, hdr 3, fractality 0); 180 cr no tier M
- Por quê: o upscale **preserva a composição e o produto** e só eleva o acabamento. Gerar do zero com Nano Banana redesenha o produto.
- Resultado: https://www.magnific.com/app/creation/aF75NF3fSh (aguardando revisão)
