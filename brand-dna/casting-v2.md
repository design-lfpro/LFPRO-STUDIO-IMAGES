---
status: planned-v2
---

# Casting V2 — Modelos com âncoras reais

## Objetivo

O cliente (LF PRO) produz ou fornece **sessões de modelo** com vários produtos. O sistema:

1. Indexa o banco de fotos (`assets/cast/`)
2. Usa a foto real como **identity lock**
3. Gera variações leves de ângulo/expressão **sem** reescrever a maquiagem aplicada de forma livre
4. Anima com Magnific i2v (micro motion)
5. Opcional futuro: face swap **leve** entre âncoras aprovadas (mesmo look de pele/make)

## O que o cliente precisa enviar

Por modelo (`model_id`):

| Asset | Obrigatório | Notas |
|-------|-------------|-------|
| 3–6 fotos rosto 3/4 e frente | Sim | Luz de estúdio consistente |
| 1–2 full/meio corpo | Não | Holding product |
| Fotos **com produto** na mão | Sim para T4 product | Packshot real no frame |
| Fotos **com make aplicado** | Sim se quiserem look | Não gerar make do zero |
| Consentimento / direito de uso | Sim | Contrato de imagem |
| Metadados: idade aparente, fototipo, tons de base usados | Sim | Matching de campanha |

## Estrutura

```
assets/cast/
  {model_id}/
    meta.yaml
    anchors/
      face-01.jpg
      face-02.jpg
      hold-soft-eye-01.jpg
    approved_looks/
      soft-matte-cor-05/
```

## meta.yaml (exemplo)

```yaml
model_id: lfpro-cast-01
display_name: "Modelo A (campanha 2026)"
apparent_age_range: [25, 35]
fitzpatrick_approx: [II, III]
hair: "dark brown, often pulled back"
notes: "prefer soft glam, short clean nails"
allowed_tracks: [T4-model-portrait]
forbidden: [T5-face-proof]  # até protocolo
products_featured: [po-soft-eye-claro, base-soft-matte-cor-05]
```

## Regras

- **Não** inventar modelo 100% IA como default se houver cast real.  
- Variação de rosto “um pouco”: só entre âncoras do **mesmo** model_id aprovadas.  
- T5 continua bloqueado até protocolo de before/after.

## Status

Aguardando banco de imagens do cliente. V1 não depende disto.
