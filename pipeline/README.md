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
| **Vídeo i2v** | **Kling 3.0** ou **Seedance 2.0** (flexível) | Escolher por custo/fila no `simulate` · 720p entrega · 1080p se pedido. **Proibido:** Seedance 1.5 |

Doc completo: `brand-dna/01-modelos-magnific.md`

```
packshot real
    → Nano Banana: START frame + END frame (9:16)  OU  composite
    → Rita Still Verifier (visão) — APPROVE ou REROLL
    → checkpoint stills (humano se quiser)
    → simulate Kling 3.0 + Seedance 2.0 → escolher mais barato/rápido
    → gerar com keyframes.start + keyframes.end (nunca só start)
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
[8] still-verify          → Rita (visão) — APPROVE_VIDEO | REROLL_* | FALLBACK_COMPOSITE
[9] checkpoint-stills     → só aprova com still-verify.md = APPROVE_VIDEO
[10] motion-engineer      → prompts Kling/Seedance i2v por cena
[11] generate-clips       → Magnific (simulate → approve → generate)
[12] checkpoint-clips
[13] ffmpeg-editor        → concat, grade leve, end card, loudnorm, 9:16
[14] reviewer             → QC checklist track + brand
[15] checkpoint-delivery
```

## Princípios (herdados OpenSquad vox/edit-videos)

1. **Barato antes de caro** — texto → still Nano Banana → vídeo Kling/Seedance  
2. **Checkpoints** antes de gastar crédito em i2v  
3. **`simulate`** antes de todo generate de vídeo — comparar Kling 3.0 x Seedance 2.0 e escolher o mais barato/rápido  
4. **Packshot real vence** packaging gerado se logo falhar  
5. **max_review_cycles: 2**  
6. **Modelos fixos na lista aprovada** — vídeo pode alternar entre Kling 3.0/Seedance 2.0 por custo, mas sem "testar modelo novo porque sim" (Hailuo, Wan, Seedance 1.5 etc.) no V1

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

## Scripts

| Script | Função | Status |
|--------|--------|--------|
| `scripts/resolve_packshot.py` | handle → path 01.* | ✅ implementado |
| `scripts/composite_dark_hero.py` | packshot real + fundo dark-studio + sombra, zero IA (fallback `FALLBACK_COMPOSITE` da Rita / strategy `packshot-composite` da Sofia) | ✅ implementado (requer Pillow + numpy) |
| `scripts/magnific_still.py` | generate image + download | a implementar |
| `scripts/magnific_i2v.py` | simulate + generate + poll | a implementar |
| `scripts/ffmpeg_assemble.sh` | concat + loudnorm + endcard | a implementar |

## Referência de API Magnific

Vault: `00-inbox/magnific-kling-video-api.md` + mapa de créditos `magnific-plano-premium-mais-mapa.md`.

Conta EcoUp Premium+ — sempre reportar `totalCreditsCost` do simulate.
