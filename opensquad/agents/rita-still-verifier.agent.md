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
- Qualquer FAIL em 1–3 ou 7 → **não** chama Seedance
- max 2 re-rolls por frame
- Se 2 fails → `FALLBACK_COMPOSITE` (packshot real no dark) e re-verifica

## Modo lineup multi-produto (N SKUs na mesma cena)

Ver `brand-dna/04-multi-product-lineup.md`. Checklist muda de por-frame pra **por-produto** — sem isso, 1 produto quebrado passa despercebido no meio de outros 9 aprovados.

| Produto | Forma/logo (1–3) | Escala | Obs |
|---|---|---|---|
| ... um linha por SKU na cena ... | PASS/FAIL | PASS/FAIL | |

- Qualquer FAIL de forma/logo num produto → esse produto específico precisa de re-roll ou retouch mascarado; não invalida os outros já PASS.
- Mesmo limite: **max 2 re-rolls por produto**. Na 3ª falha, `FALLBACK_COMPOSITE` só daquele item (retouch mascarado ou overlay do packshot real) — não regenerar a cena inteira de novo.
- Regra crítica: depois que uma rodada aprova um subconjunto de produtos, uma nova chamada de `images_generate` **não preserva** esses aprovados — é geração nova do zero. Registrar explicitamente quais produtos já passaram antes de decidir o próximo passo, pra não achar que "só falta corrigir X" quando na verdade tudo está em risco de novo.
