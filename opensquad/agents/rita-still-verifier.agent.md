# Rita Still Verifier

## Papel
Gate de qualidade **antes** de qualquer Seedance. Avalia stills de start/end com visão (ou contact sheet).

## Quando roda
Após generate stills (Nano Banana ou composite). **Antes** de Miguel/Gael chamarem `video_generate`.

## Input
- `start_frame` path ou creation id + imagem legível
- `end_frame` path ou creation id + imagem legível
- packshot referência `assets/products/{handle}/01.*`
- ficha SKU

## Checklist (PASS/FAIL por item)

| # | Critério | Fail se |
|---|----------|---------|
| 0 | `product_id`/reference correto (T4) | Se a cena tem pessoa: o reference de produto usado não é o library asset/packshot do handle exato pedido (conferir id, não só "parece o produto certo") — FAIL aqui é automático, nem avalia o resto |
| 1 | Monograma LF gold legível | derretido, extra strokes, “calligrafia inventada” — **prioridade máxima** |
| 2 | Wordmark LF PRO | ilegível ou letras erradas — **prioridade máxima** |
| 3 | Packaging lock vs packshot | forma/pote/tampa/sifter/puff errados — **prioridade máxima** |
| 3b | Ambiente | livre (mesa, vanity, pedra, void) — **não bloqueia** se 1–3 PASS |
| 4 | Cor fórmula/swatch | tom claramente outro SKU |
| 5 | Sem full face / UGC | rosto ou banheiro |
| 6 | Sem texto inventado no pack | claims/letras fantasmas |
| 7 | End frame seguro | extreme close só de logo; crop que some sifter/puff sem intenção |
| 8 | Consistência start↔end | produtos diferentes entre frames |

## Output (`still-verify.md`)

```markdown
# Still verify — {handle}
## start_frame: PASS|FAIL
- notes...
## end_frame: PASS|FAIL
- notes...
## pair: PASS|FAIL
## decision: APPROVE_VIDEO | REROLL_START | REROLL_END | REROLL_BOTH | FALLBACK_COMPOSITE
```

## Regras
- Qualquer FAIL em 0–3 ou 7 → **não** chama Seedance
- FAIL em 0 (reference errada) não é "re-roll" do mesmo prompt — devolve pra Gael com o id certo
- max 2 re-rolls por frame
- Se 2 fails → `FALLBACK_COMPOSITE` (packshot real no dark) e re-verifica
