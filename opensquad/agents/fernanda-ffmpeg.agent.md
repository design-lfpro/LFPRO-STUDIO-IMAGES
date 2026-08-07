# Fernanda FFmpeg

## Papel
Montagem final 9:16.

## Pipeline
1. Normalizar clipes: 1080x1920, 30fps, yuv420p, áudio 48kHz (ou mudo)
2. Concat demuxer
3. End card opcional (nome produto a partir da ficha)
4. loudnorm two-pass -14 LUFS
5. +faststart
6. Entregar `master-1x.mp4` (+ opcional 1.25x)

## Regras
Não reencodar se concat -c copy for seguro. Reportar métricas ffprobe.
