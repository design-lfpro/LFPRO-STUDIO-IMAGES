# Step 07 — still-verify

Rita (Rita Still Verifier) avalia start/end com visão **antes** do checkpoint humano e **antes** de qualquer i2v.

## Input
- `start_frame` / `end_frame` (path ou creation id) gerados no step 06
- packshot referência `assets/products/{handle}/01.*`
- ficha SKU

## Output
`still-verify.md` — ver checklist completo em `opensquad/agents/rita-still-verifier.agent.md`.

`decision: APPROVE_VIDEO | REROLL_START | REROLL_END | REROLL_BOTH | FALLBACK_COMPOSITE`

## Regra
- FAIL em logo/packaging/end-close → **não** segue pro checkpoint-stills como aprovado; volta pro step 06 (re-roll, máx 2) ou aciona `FALLBACK_COMPOSITE`
- `FALLBACK_COMPOSITE` → rodar `pipeline/scripts/composite_dark_hero.py {handle}` (packshot real sobre dark, zero IA) e re-verificar
- Sem `still-verify.md` com `decision: APPROVE_VIDEO`, o step 08 (checkpoint-stills) não aprova e o step 09 (motion) não roda

Ver squad.yaml e pipeline/README do projeto pai.
