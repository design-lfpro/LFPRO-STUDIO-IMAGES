---
family: essential-lips
tags: [casting, magnific, nano-banana, ai-model]
status: dna-v1-scaffold
updated: 2026-08-13
---

# Casting — trio de modelos (tons de pele) — Essential Lips

Passo 1 da campanha, decidido em briefing: gerar **3 modelos base por tom de pele** (Light / Medium / Dark), independentes de tonalidade de produto. Passo 2 (futuro, ainda não feito): adaptar cada modelo às 3 tonalidades do produto escolhidas (`Rose`, `Carmim`, `Wine` — ver [[_family]]), aplicando a cor do batom nos lábios de cada uma.

## Por que IA e não cast real

`brand-dna/casting-v2.md` diz para preferir cast real do cliente e não inventar modelo 100% IA como default **quando houver cast real disponível**. Não há cast real para Essential Lips ainda (`assets/cast/` vazio). O próprio LF PRO já usou esse padrão de trio 100% IA gerado via Magnific/Nano Banana no lançamento **Sculpt Brow** (Drive: pasta "Sculpt Brow", arquivos `SCULPT-BROW-MODELO-LIGHT/MEDIUM/DARK.png`, gerados via `magnific_modelo-sem-acessorios-...`) — este casting segue a mesma gramática visual já validada pela marca, mas com identidades novas (não reaproveita o rosto das modelos do Sculpt Brow).

## Gramática visual (herdada do precedente Sculpt Brow)

- Retrato beauty 3/4, olhando para câmera, ombro à mostra (sem roupa visível no enquadramento)
- Fundo neutro quente (bege/tan), um feixe de luz diagonal suave cruzando o rosto
- Pele com viço/dewy, make natural glam (sobrancelha definida, olho em tons bronze suaves)
- **Lábios nude limpos, sem cor de batom aplicada** — canvas base para a Etapa 2
- Still still (não still de vídeo): 9:16, foco raso, still fotorrealista

## Modelo

- **Frames/stills:** Google Nano Banana Pro (`imagen-nano-banana-2`) @ 2k — trava V1 (`brand-dna/01-modelos-magnific.md`)
- Custo: 75 créditos/imagem × 3 = 225 créditos (plano Premium+, unlimited não estava ativo nesta sessão)

## Trio gerado (2026-08-13)

| Modelo | Tom de pele | Magnific creation | Magnific library (character, p/ reuso via reference) | webUrl |
|--------|-------------|--------------------|--------------------------------------------------------|--------|
| Modelo A | Claro (light) | `p88i1K3ehw` | `essential-lips-modelo-light` (id 2164367) | https://www.magnific.com/app/creation/p88i1K3ehw |
| Modelo B | Médio/oliva (medium) | `XmmZjgLBfo` | `essential-lips-modelo-medium` (id 2164368) | https://www.magnific.com/app/creation/XmmZjgLBfo |
| Modelo C | Escuro (dark) | `MBBNK4ZDCm` | `essential-lips-modelo-dark` (id 2164369) | https://www.magnific.com/app/creation/MBBNK4ZDCm |

Organizados no projeto Magnific **"LFPro Studio — Essential Lips"**. Registrados também como **library characters** (`type: character`) para permitir identity-lock nas próximas gerações (Etapa 2), passando `references: [{type: "character", identifier: "<id>"}]` em `images_generate`.

### Prompt base (EN) por tom — variar só a descrição de pele/cabelo, manter o resto fixo

```
Premium beauty editorial portrait for a luxury cosmetics brand. Young adult woman, {SKIN_TONE_DESC}. 3/4 turned beauty portrait, bare shoulder, looking toward camera. Warm neutral studio backdrop (soft beige/tan), one soft diagonal beam of directional light crossing the face, dewy luminous skin with visible healthy texture, soft natural glam makeup (groomed brows, subtle bronze eye, neutral nude glossy lips with NO lipstick color yet — clean canvas lips). Sharp focus on face and lips, shallow depth of field, photorealistic, high-end cosmetics campaign photography, no text, no logo, no product in frame.
```

| Tom | `{SKIN_TONE_DESC}` usado |
|-----|--------------------------|
| Light | LIGHT/FAIR skin tone, fair complexion, light hair (blonde or light brown), light-colored eyes |
| Medium | MEDIUM/OLIVE-TAN skin tone, warm medium brown complexion, dark brown wavy hair |
| Dark | DEEP/DARK skin tone, rich deep brown complexion, dark wavy/coily black hair |

## Pendências / próximos passos

1. **Aprovação humana** do trio (checkpoint) antes de avançar — ver imagens nos links acima
2. **Etapa 2:** adaptar cada uma das 3 modelos às 3 tonalidades do produto (`Rose`, `Carmim`, `Wine`), aplicando a cor correspondente nos lábios via edição/composite guiado pelo character de cada modelo — só depois que o packshot oficial por tom chegar (ver pendência em [[_family]])
3. Não gerar vídeo (i2v) a partir desse trio ainda — está fora do T1/T2 V1 até termos o still final com produto aplicado
4. Baixar os PNGs originais do Magnific para `assets/cast/essential-lips/` quando a política de rede da sessão permitir (nesta sessão o host de CDN do Magnific — `pikaso.cdnpk.net` — foi bloqueado pelo proxy da organização; os assets ficam preservados no projeto/library do Magnific até lá)
