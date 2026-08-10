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
- Padrão de persona (idade, diversidade de tom) e padrão de fidelidade de textura: ver `brand-dna/04-modelos-realismo.md` — obrigatório antes de aprovar qualquer `model_id`.

## Elenco no Magnific (character reference)

Além de `assets/cast/{model_id}/` (arquivo), cada âncora aprovada deve ganhar um **character** na biblioteca do Magnific (`library_create` / `library_list type=character`), para travar rosto em `images_generate` e `video_generate` via `references: [{type:"character", identifier:<id>}]`. Hoje só existe 1 character salvo (`lu-golden`, provável âncora da fundadora) — nenhum elenco diverso ainda cadastrado.

## Auditoria de material já existente (2026-08-10)

Levantamento em site, Instagram, repo e Google Drive — detalhado em `brand-dna/04-modelos-realismo.md §2`. Resumo:

- Packshots do site (`assets/products/`) não têm pessoa — não servem de âncora.
- Drive tem **histórico real de casting** de campanhas 2024–2025: cada lançamento contratou 3+ modelos, uma por bloco de tom (claro/médio/escuro), via agência (Contrato Direto, Container Casting, Fire Models). Isso já é o padrão de diversidade pedido — falta só formalizar como `assets/cast/`.
- Já existem testes manuais de still/i2v com modelo feitos direto no Magnific fora deste squad (fora de qualquer QC documentado) — precisam ser trazidos para o pipeline com gate da Nina Pele.

## Status

- [x] Auditoria de material do cliente (site/IG/Drive/Magnific) — 2026-08-10, ver `brand-dna/04-modelos-realismo.md`
- [ ] Cliente/marca aprova piso de idade (30+) e escolhe 2–4 modelos do histórico para virar cast oficial
- [ ] Confirmar direito de uso por IA dos contratos antigos antes de promover foto de campanha para `assets/cast/`
- [ ] Banco de imagens formal em `assets/cast/` (ainda não existe no repo)

V1 (T1/T2, sem rosto) não depende disto.
