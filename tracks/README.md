---
tags: [lfpro-studio, tracks]
---

# Tracks — mapa

Um **track** define job criativo, inputs obrigatórios, shot list template, motores Magnific e critérios de QC.

| ID | Pasta | V1? |
|----|-------|-----|
| T1 | [[T1-product-hero/README]] | Sim |
| T2 | [[T2-texture-macro/README]] | Sim |
| T3 | [[T3-tools-hands/README]] | Spec only |
| T4 | [[T4-model-portrait/README]] | Spec only (V2) |
| T5 | [[T5-face-proof/README]] | Spec only (V3 locked) |

## Escolha automática (orquestrador)

```
if category in [Pó, Base, Corretivo, Batom, Sombra, Blush, Contorno, Máscara, Primer, Hidratante, Sérum]
  and no hands/face required → default T1
if claim_texture or powder/cream visible → suggest T2 as B-roll
if category in [Pincel, Esponja] → T1 or T3
if cast_photo provided → T4
if before_after requested → T5 (reject if not unlocked)
```
