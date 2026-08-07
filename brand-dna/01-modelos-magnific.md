---
tags: [lfpro-studio, magnific, seedance, nano-banana]
status: locked-v1
updated: 2026-08-06
decided_by: Jonathan
---

# Modelos Magnific — LOCK V1

Stack **fixada** do LFPro Studio. Agents **não** escolhem modelo livremente no V1.

| Etapa | Modelo | Slug Magnific (referência) | Papel |
|-------|--------|----------------------------|-------|
| **Frames / stills** | **Google Nano Banana 2 Lite → Pro** | `imagen-nano-banana-2-lite` (tentativa 1, ~60cr) → `imagen-nano-banana-2` @ 2k (escalada, ~75cr) · fallback `imagen-nano-banana-2-flash` | Keyframes start/end |
| **Vídeo (i2v) DEFAULT** | **Kling 3.0** | `kling-30` · 720p · first+last | Product motion (melhor custo/qualidade no A/B 2026-08-06) |
| **Vídeo premium** | **Seedance 2.0** ou **Veo 3.1** | `bytedance-seedance-pro-2.0` · `google-veo3_1` | Flagship; mais créditos |
| **NÃO usar** | Seedance 1.5 **Draft** | `bytedance-seedance-pro-1.5` + Draft | Qualidade baixa (teste falhou) |

A/B: `output/ab-test-video-models-20260806/COMPARISON.md`

Plataforma: **Magnific only** (não kie.ai neste projeto).

---

## 1. Nano Banana — imagens / frames

### Política de escalada (decidido por Jonathan, 2026-08-07)
**Sempre tentar primeiro `imagen-nano-banana-2-lite`** (mais barato, ~60cr, mais rápido ~11s). Só escalar para `imagen-nano-banana-2` Pro (~75cr, ~50s) **se o Lite não atender** — falhou no gate de verificação (logo/monograma incoerente, engraving duplicado, geometria do produto errada, etc). Não pular direto pro Pro "por segurança"; o Lite é a tentativa 1 obrigatória.

⚠️ Nota de custo — **plano vs. execução via agente** (confirmado via `account_balance` em 2026-08-07):
- Plano é **Premium+ com unlimited mode** (`isUnlimitedMode: true`) — no app Magnific aberto direto no navegador, Nano Banana 2 Lite/Pro/Flash aparecem com **∞** e não descontam crédito.
- **Mas** toda geração feita por este squad/agente roda via MCP, e nessa sessão `unlimitedAppliesHere: false` — ou seja, **mesmo modelo, mesmo plano, mas via agente sempre desconta do pool de créditos** (confirmado por `simulate_cost`: Lite ~60cr, Pro ~75cr). Isso não é bug, é como a Magnific fatura chamadas de API/MCP separado do uso manual no app.
- Prática: reportar credits real de cada geração no review.md. Se o volume de reroll ficar alto, considerar gerar manualmente no app (unlimited) e subir como upload — mas isso tira o still do fluxo automatizado do squad.

### Por que
- Google, bom em produto + fidelidade visual
- Ideal pra gerar frames de cena **com reference do packshot**

### Defaults V1

| Param | Valor |
|-------|--------|
| Modelo (tentativa 1) | `imagen-nano-banana-2-lite` |
| Escalada (se Lite falhar no gate) | `imagen-nano-banana-2` (Pro) @ 2k |
| Fallback se fila/erro | `imagen-nano-banana-2-flash` |
| Resolução (Pro) | **2k** (equilíbrio qualidade/custo; evita 4k pago) |
| Aspect still de cena | **9:16** quando for frame de vídeo |
| Input | **sempre** packshot `assets/products/{handle}/01.*` como referência (i2i / ref image) |
| Proibido | Text-to-image **sem** reference do packaging (redezenha logo) |

### Quando NÃO usar Nano Banana
- Se o still for **composite determinístico** do packshot real no fundo dark (zero risco de logo) — aí skip generate de imagem e usa o composite como frame
- Estratégia da Sofia: `packshot-composite` | `nano-banana-i2i` | `hybrid`

---

## 2. Seedance 1.5 Pro — vídeo

### Por que
- Um dos melhores da Magnific pra motion controlado de produto
- OpenSquad já tem gramática madura de Seedance (empty frame / first-last no vox; aqui adaptar a **product lock**)
- Draft tier na Magnific pode ser **ilimitado** (com ou sem áudio) — bom pra teste
- 720p/1080p cobram créditos — usar no master final

### Defaults V1

| Param | Valor |
|-------|--------|
| Modelo | **Seedance 1.5 Pro** (`bytedance-seedance-pro-1.5`) |
| Modo teste / draft | resolution **`Draft`** |
| Modo entrega | **`720p`** default; **`1080p`** se briefing `final` |
| Duração por clipe | **4–5s** |
| Aspect | **9:16** |
| Áudio nativo Seedance | **off** no V1 |
| Input | **OBRIGATÓRIO first + last frame** (nunca só start) |
| Motion | pó / luz / parallax mínimo; **sem** extreme close no logo |
| Simulate / créditos | reportar custo; sessão MCP pode consumir créditos mesmo Premium+ |

### First + last frame (OBRIGATÓRIO no V1)

```text
keyframes.start = still A (aprovado pelo verificador)
keyframes.end   = still B (aprovado pelo verificador)
```

| Modo | Start | End | Quando |
|------|-------|-----|--------|
| **hold-lock** | hero | **mesmo** hero | máximo anti-drift |
| **pair** | hero wide | hero leve variação (ângulo/pó, **packaging completo ainda visível**) | default T1 |
| **texture** | hero | macro swatch/pote (ambos QC) | T2 |

**Proibido no end frame:** extreme close só de logo/tampa, crop que corta monograma ou sifter.

### Prompt motion (regra)
```
Interpolate ONLY between the exact start and end frames provided.
Preserve packaging and gold LF logo from both keyframes.
No morphing, no melting, no inventing a new final pose.
Camera motion minimal; never extreme close-up on lid logo.
Optional soft powder dust only if consistent with frames.
```

### Gate de verificação (ANTES do Seedance)

Agente **Rita / still-verifier** avalia cada still com visão:

1. Logo monograma LF legível e coerente com packshot  
2. Wordmark LF PRO ok (tampa e/ou puff)  
3. Sifter / forma do pote / puff presentes se no packshot  
4. Cor do tom (pó/creme) coerente  
5. Sem rosto / full-face (T1/T2)  
6. Sem texto hallucinado no packaging  
7. End frame **não** é extreme close de logo  

**PASS** → Seedance. **FAIL** → re-roll still (máx 2) ou composite packshot real. **Nunca** gerar vídeo com still FAIL.
---

## 3. O que fica de fora no V1 (não misturar)

| Modelo | Status |
|--------|--------|
| Kling 2.5 / 3.0 | Backup só se Seedance falhar 2× no mesmo clipe |
| Hailuo / Wan | Não default |
| Flux / Seedream / GPT-Image | Não default de still (Nano Banana locked) |
| Veo | Não V1 product |

Se backup Kling for necessário: anotar no `review.md` e no `magnific-requests.json`.

---

## 4. Fluxo de motores (mix travado)

```
packshot real (site)
        │
        ▼
  Sofia decide strategy
   ├── packshot-composite (FFmpeg/Python) → still final sem IA
   └── Nano Banana 2k + ref packshot → still de cena
        │
        ▼
  checkpoint stills (humano)
        │
        ▼
  Seedance 1.5 Pro i2v (Draft teste → 720p/1080p final)
        │
        ▼
  checkpoint clips
        │
        ▼
  FFmpeg montagem 9:16
```

---

## 5. Custo (referência Premium+ EcoUp)

| Etapa | Expectativa |
|-------|-------------|
| Nano Banana 2k | Ilimitado (dentro do cap unlimited mensal) |
| Seedance Draft | Ilimitado no tier draft |
| Seedance 720p | ~400 cr / clip (mapa mai/2026 — sempre simulate) |
| Seedance 1080p | ~440 cr / clip (+ áudio x2 se ligar) |

Fonte: `00-inbox/magnific-plano-premium-mais-mapa.md`

---

## 6. Instrução para agents

- **Sofia Still:** modelo de imagem = Nano Banana apenas  
- **Miguel Motion:** modelo de vídeo = Seedance 1.5 Pro apenas  
- **Gael Magnific:** executa só esses dois; não “melhorar” com outro modelo sem override humano no briefing  
- **Léo / Briefing:** pergunta opcional `qualidade_video: draft | 720p | 1080p` (default draft em teste, 720p em entrega)
