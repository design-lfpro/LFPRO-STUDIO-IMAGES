---
pipeline: lfpro-studio-social-copy-v1
status: framework-ready
engine: agentes de texto (sem geração de imagem/vídeo neste fluxo)
---

# Pipeline — Texto para Social (copy)

Fluxo de texto/copy para posts sociais (legenda, gancho, layout). Não gera imagem/vídeo — quando a peça exige asset visual, o pacote final é repassado ao pipeline V1 de vídeo (`pipeline/pipeline.yaml`) via `Léo Orquestrador` / `Gael Magnific`.

## Fluxo

```
[1] pauta (opcional)    → Vini Estrategista — só se o tema não vier definido no pedido
[2] ganchos              → Theo Ganchos — mínimo 5 opções de gancho/headline
[3] legenda              → Bia Legendas — 3 variações (direta, storytelling, provocativa) + hashtags
[4] revisão              → Duda Revisão — gramática, tom, claims não verificados sinalizados
[5] layout               → Cacá Layout — composição visual (texto/imagem/CTA)
[6] checkpoint-entrega   → Léa Orquestradora entrega pacote: texto final + layout + (se aplicável) handoff visual
```

Orquestradora: **Léa Orquestradora** (`opensquad/agents/lea-orquestradora.agent.md`).

## Princípios

1. **Claims só da ficha do produto** (`products/{family}/{handle}.md`, `body_text`) — nenhum agente de texto inventa benefício.
2. **Tom de voz**: `brand-dna/03-tom-de-voz-copy.md` (complementa `00-brand-dna.md`).
3. **Léa não pula etapas** — cada agente cobre uma responsabilidade; claim fora da ficha volta para revisão (Duda) antes de seguir adiante.
4. **Handoff visual opcional** — se a peça exigir imagem/vídeo gerado, o pacote passa para o pipeline V1 (`pipeline/pipeline.yaml`).

## Input mínimo de um run

```yaml
handle: po-soft-eye-claro     # obrigatório — identifica a ficha/claims permitidos
tema: null                    # opcional — se vazio, Vini Estrategista sugere pauta
formato: reels                # reels | carrossel | post-unico | stories
objetivo: vender               # vender | engajar | informar
```

## Artefatos por run

```
output/{timestamp}/social-copy/
  pauta.md            # se step 1 rodou
  ganchos.md
  legenda.md
  revisao.md
  layout.md
  pacote-final.md
```

## Scripts

Nenhum script dedicado — fluxo 100% agentes de texto (sem chamada Magnific/FFmpeg neste pipeline).
