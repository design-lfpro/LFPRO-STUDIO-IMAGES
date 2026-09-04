---
tags: [lfpro-studio, magnific, seedance, kling, nano-banana]
status: locked-v1
updated: 2026-09-04
decided_by: Jonathan
---

# Modelos Magnific — LOCK V1

Stack **fixada** do LFPro Studio pra stills. Pra vídeo, o V1 trava a **dupla** de melhor custo-benefício e deixa a escolha entre elas livre por run — agents não "testam modelo novo por conta própria", mas também não ficam presos a um único motor de vídeo.

| Etapa | Modelo | Slug Magnific (referência) | Papel |
|-------|--------|----------------------------|-------|
| **Frames / stills** | **Google Nano Banana Pro** | `imagen-nano-banana-2` @ 2k · fallback `imagen-nano-banana-2-flash` | Keyframes start/end |
| **Vídeo (i2v) DEFAULT — flexível** | **Kling 3.0** *ou* **Seedance 2.0** | `kling-30` · `bytedance-seedance-pro-2.0` | 720p · first+last · escolher por custo/fila no `simulate` |
| **Vídeo premium** | **Veo 3.1** | `google-veo3_1` | Flagship; só se briefing pedir explicitamente (mais créditos) |
| **NÃO usar** | Seedance 1.5 (com ou sem **Draft**) | `bytedance-seedance-pro-1.5` | Qualidade baixa (reprovado em A/B 2026-08-06) |

A/B: `output/ab-test-video-models-20260806/COMPARISON.md`

Plataforma: **Magnific only** (não kie.ai neste projeto).

---

## 1. Nano Banana — imagens / frames

### Por que
- Google, bom em produto + fidelidade visual
- Tier Magnific Premium+: **1k e 2k ilimitados** em `imagen-nano-banana-2` / flash (4k cobra ~150 cr)
- Ideal pra gerar frames de cena **com reference do packshot**

### Defaults V1

| Param | Valor |
|-------|--------|
| Modelo | `imagen-nano-banana-2` |
| Fallback se fila/erro | `imagen-nano-banana-2-flash` |
| Resolução | **2k** (equilíbrio qualidade/custo; evita 4k pago) |
| Aspect still de cena | **9:16** quando for frame de vídeo |
| Input | **sempre** packshot `assets/products/{handle}/01.*` como referência (i2i / ref image) |
| Proibido | Text-to-image **sem** reference do packaging (redezenha logo) |

### Quando NÃO usar Nano Banana
- Se o still for **composite determinístico** do packshot real no fundo dark (zero risco de logo) — aí skip generate de imagem e usa o composite como frame
- Estratégia da Sofia: `packshot-composite` | `nano-banana-i2i` | `hybrid`

---

## 2. Kling 3.0 / Seedance 2.0 — vídeo (flexível)

### Por que
- Os dois com melhor custo/qualidade no A/B 2026-08-06 pra motion controlado de produto
- Escolha entre os dois é por **custo/fila no momento do run** (rodar `simulate` nos dois se houver dúvida) — não é "testar modelo novo", é usar a dupla já validada
- OpenSquad já tem gramática madura de i2v (empty frame / first-last no vox; aqui adaptada a **product lock**)
- 720p/1080p cobram créditos — usar 720p em teste, 1080p só no master final se pedido

### Defaults V1

| Param | Valor |
|-------|--------|
| Modelo | **`kling-30`** ou **`bytedance-seedance-pro-2.0`** (escolher por custo/fila) |
| Modo teste | **`720p`** (draft quando o modelo escolhido oferecer) |
| Modo entrega | **`720p`** default; **`1080p`** se briefing `final` |
| Duração por clipe | **4–5s** |
| Aspect | **9:16** |
| Áudio nativo | **off** no V1 |
| Input | **OBRIGATÓRIO first + last frame** (nunca só start) |
| Motion | pó / luz / parallax mínimo; **sem** extreme close no logo |
| Simulate / créditos | reportar custo dos dois candidatos antes de gerar; sessão MCP pode consumir créditos mesmo Premium+ |

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

### Gate de verificação (ANTES do vídeo)

Agente **Rita / still-verifier** avalia cada still com visão:

1. Logo monograma LF legível e coerente com packshot  
2. Wordmark LF PRO ok (tampa e/ou puff)  
3. Sifter / forma do pote / puff presentes se no packshot  
4. Cor do tom (pó/creme) coerente  
5. Sem rosto / full-face (T1/T2)  
6. Sem texto hallucinado no packaging  
7. End frame **não** é extreme close de logo  

**PASS** → segue pro i2v (Kling 3.0 ou Seedance 2.0). **FAIL** → re-roll still (máx 2) ou composite packshot real. **Nunca** gerar vídeo com still FAIL.
---

## 3. O que fica de fora no V1 (não misturar)

| Modelo | Status |
|--------|--------|
| Seedance 1.5 (Draft ou não) | Proibido — reprovado no A/B |
| Kling 2.5 | Não default (usar Kling 3.0) |
| Hailuo / Wan | Não default |
| Flux / Seedream / GPT-Image | Não default de still (Nano Banana locked) |
| Veo 3.1 | Não é default de vídeo — só premium sob pedido explícito do briefing |

Se Veo 3.1 for usado: anotar no `review.md` e no `magnific-requests.json`.

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
  Kling 3.0 ou Seedance 2.0 i2v (escolha por custo/fila → 720p/1080p final)
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
| Kling 3.0 720p | Cobra créditos — **sempre `simulate` antes de gerar** |
| Seedance 2.0 720p | Cobra créditos — **sempre `simulate` antes de gerar** |
| 1080p (qualquer um) | Mais caro que 720p (+ áudio x2 se ligar) |

Como o custo dos dois motores muda com frequência, **não fixar número aqui** — rodar `simulate_cost` nos dois candidatos no momento do run e registrar o valor real em `review.md`. Referência de mapa de créditos: `00-inbox/magnific-plano-premium-mais-mapa.md`.

---

## 6. Instrução para agents

- **Sofia Still:** modelo de imagem = Nano Banana apenas  
- **Miguel Motion:** modelo de vídeo = Kling 3.0 **ou** Seedance 2.0 — escolhe por custo/fila do `simulate`, nunca Seedance 1.5  
- **Gael Magnific:** executa só os modelos desta tabela; não "melhorar" com outro modelo (Hailuo, Wan, Veo fora de premium, etc.) sem override humano no briefing  
- **Léo / Briefing:** pergunta `modelo_video: kling-30 | seedance-2.0` (opcional, default = mais barato no `simulate` do dia) + `qualidade_video: 720p | 1080p` (default 720p em entrega)
