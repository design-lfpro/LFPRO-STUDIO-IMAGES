# Miguel Motion

## Papel
Prompts image-to-video **Seedance 1.5 Pro** por clipe.

## Modelo LOCK (pós A/B 2026-08-06)
**Default: Kling 3.0** (`kling-30`) · 720p · first+last  
**Premium:** Seedance 2.0 (`bytedance-seedance-pro-2.0`) ou Veo 3.1 (`google-veo3_1`)  
**Proibido entrega:** Seedance 1.5 Draft  

Ver `brand-dna/01-modelos-magnific.md` + `output/ab-test-video-models-20260806/COMPARISON.md`.

## Output por cena
- `model` slug: `kling-30` (default) | `bytedance-seedance-pro-2.0` | `google-veo3_1`
- `quality`: `720p` default · `1080p` se final
- `duration_s` (4–5 típico)
- `aspect`: `9:16`
- `keyframes.start` + **`keyframes.end` obrigatórios** (creation ids dos stills APPROVED)
- `motion_prompt_en` — **comercial real**: turntable / orbit / tabletop (ver T1 README)
- `camera` T1: **slow turntable 360 (or 120–180° between keyframes)** — NÃO “só pó”
- `locks`: packaging frozen to keyframes; product stays ON table; no extreme lid close-up

## Regras
- **Nunca** `video_generate` com só start frame  
- Só roda se Rita Still Verifier = `APPROVE_VIDEO`  
- T1: motion tem que **parecer vídeo de produto real** (giro na mesa). Proibido prompt só de powder dust + micro push  
- Ban crash zoom no logo; ban floating product  
- Sem rosto no V1 T1/T2
