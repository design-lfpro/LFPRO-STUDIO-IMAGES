---
pipeline: lfpro-studio-v1
status: framework-ready
engine: magnific (nano-banana + seedance) + ffmpeg
---

# Pipeline V1 — Product Studio Video

## Modelos LOCK (não negociar no V1)

| Etapa | Modelo | Detalhe |
|-------|--------|---------|
| **Stills / frames** | **Google Nano Banana** (`imagen-nano-banana-2` @ 2k) | Sempre com ref do packshot |
| **Vídeo i2v** | **Seedance 1.5 Pro** | Draft teste · 720p entrega · 1080p se pedido |

Doc completo: `brand-dna/01-modelos-magnific.md`

```
packshot real
    → Nano Banana: START frame + END frame (9:16)  OU  composite
    → Rita Still Verifier (visão) — APPROVE ou REROLL
    → checkpoint stills (humano se quiser)
    → Seedance 1.5 Pro com keyframes.start + keyframes.end (nunca só start)
    → checkpoint clips
    → FFmpeg master 9:16
```

## Fluxo

```
[1] checkpoint-briefing
[2] load-context          → brand-dna + ficha + packshot
[3] product-analyst       → vision notes do packshot (cores, logo, riscos)
[4] creative-director     → shot list do track
[5] checkpoint-shotlist
[6] still-engineer        → prompts still Nano Banana / composite plan
[7] generate-stills       → Magnific Nano Banana (ou packshot real composite)
[8] checkpoint-stills
[9] motion-engineer       → prompts Seedance i2v por cena
[10] generate-clips       → Magnific Seedance (simulate → approve → generate)
[11] checkpoint-clips
[12] ffmpeg-editor        → concat, grade leve, end card, loudnorm, 9:16
[13] reviewer             → QC checklist track + brand
[14] checkpoint-delivery
```

## Princípios (herdados OpenSquad vox/edit-videos)

1. **Barato antes de caro** — texto → still Nano Banana → vídeo Seedance  
2. **Checkpoints** antes de gastar crédito em i2v  
3. **`simulate`** antes de todo generate Seedance  
4. **Packshot real vence** packaging gerado se logo falhar  
5. **max_review_cycles: 2**  
6. **Modelos fixos** — sem “testar Kling porque sim” no V1

## Artefatos por run

```
output/{timestamp}/
  briefing.md
  shotlist.json
  stills/
  clips/
  prompts/
  master-1x.mp4
  master-reels-1.25x.mp4   # opcional
  review.md
  state.json
```

## Scripts (a implementar)

| Script | Função |
|--------|--------|
| `scripts/resolve_packshot.py` | handle → path 01.* |
| `scripts/composite_dark_hero.py` | packshot + fundo dark + sombra |
| `scripts/magnific_still.py` | generate image + download |
| `scripts/magnific_i2v.py` | simulate + generate + poll |
| `scripts/ffmpeg_assemble.sh` | concat + loudnorm + endcard |

## Referência de API Magnific

Vault: `00-inbox/magnific-kling-video-api.md` + mapa de créditos `magnific-plano-premium-mais-mapa.md`.

Conta EcoUp Premium+ — sempre reportar `totalCreditsCost` do simulate.
