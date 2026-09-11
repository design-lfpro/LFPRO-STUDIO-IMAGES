---
tags: [projeto, lfpro, studio, video, ia, magnific, opensquad, brand-dna]
projeto: lfpro-studio
cliente: LF PRO
status: em-construcao
created: 2026-08-06
---

# LFPro Studio — Fábrica de vídeo de produto com IA

Sistema de produção de vídeos de **estúdio / product hero** para a [[Clientes Ativos|LF PRO]], orquestrado via **OpenSquad**, geração via **Magnific** (substitui kie.ai no fluxo de product video), montagem via **FFmpeg**.

> Cliente de longa data da EcoUp. E-commerce: [lfpro.com.br](https://lfpro.com.br) · IG: [@lfpro.oficial](https://www.instagram.com/lfpro.oficial/)  
> Projetos irmãos: [[gestor-lfpro/overview|Gestor LFpro]] · [[agente-luci/overview|Agente Luci]] · [[trafego-clientes/lfpro/LFPRO|Tráfego LFPro]]

---

## Problema

A LF PRO escala conteúdo de influenciador e carrossel, mas **vídeo de produto em estúdio** (object beauty, textura, tools) é caro de repetir por SKU. Maquiagem aplicada em modelo com fidelidade de fórmula é outro nível de risco — fica na V2/V3.

## Solução (filosofia)

| Princípio | Significado |
|-----------|-------------|
| **1 squad de marca** | Não um squad por produto |
| **Produto = ficha** | `products/{family}/{handle}.md` |
| **Track = comportamento** | T1…T5 por dificuldade |
| **IA multiplica a verdade** | Packshot real ancora packaging/logo/textura |
| **IA não inventa prova** | Before/after e shade match = tracks bloqueados até protocolo |

## Roadmap de tracks

| Track | Nome | Status | Risco IA |
|-------|------|--------|----------|
| **T1** | Product hero (packshot animado / object beauty) | **V1 — ativo** | Baixo |
| **T2** | Texture macro (pó, creme, swatch) | **V1 — ativo** | Baixo–médio |
| **T3** | Tools + hands (pincel, esponja; mão sem full face) | V1.5 | Médio |
| **T4** | Model portrait (holding / beauty; âncoras de foto real) | V2 | Médio–alto |
| **T5** | Face proof (aplicação, before/after) | V3 | Muito alto |

## Estrutura do repositório

```
lfpro-studio/
├── overview.md                 ← este arquivo
├── CLAUDE.md                   ← contexto para agentes
├── brand-dna/                  ← leis da marca (fixas, globais)
├── products/                   ← fichas por família + SKU
├── tracks/                     ← T1…T5 specs
├── pipeline/                   ← steps, scripts, data do V1
├── opensquad/                  ← squad espelhado (pronto p/ /home/projects/opensquad)
├── assets/
│   ├── catalog/                ← products.json index, families, claims
│   ├── products/{handle}/      ← 552 imagens do site (packshots)
│   └── refs/                   ← frames gold Instagram (a popular)
├── _research/                  ← IG, site, referências
└── output/                     ← renders de teste
```

## Catálogo (scrape 2026-08-06)

- **91 produtos** Shopify em [lfpro.com.br](https://lfpro.com.br)
- **552 imagens** baixadas em alta resolução (~893 MB)
- Índice: `assets/catalog/products-index.json`
- Famílias: `assets/catalog/families.json`

## Stack

| Camada | Tecnologia |
|--------|------------|
| Orquestração | OpenSquad (agents + pipeline + checkpoints) |
| Geração stills/frames | Magnific → **Google Nano Banana** (`imagen-nano-banana-2` @ 2k) |
| Geração vídeo i2v | Magnific → **Seedance 1.5 Pro** (Draft teste / 720p entrega) |
| Montagem | FFmpeg (concat, loudnorm, end card, 9:16) |
| Doc modelos | [[brand-dna/01-modelos-magnific\|Modelos LOCK]] |
| Verdade do produto | Packshot oficial do site (nunca redesenhar packaging) |

## Como rodar (quando pipeline V1 estiver wired)

```bash
# No workspace OpenSquad (VPS):
# /home/projects/opensquad  (squad copiado de opensquad/ deste projeto)
/opensquad run lfpro-studio
```

Input mínimo V1:

```yaml
handle: po-soft-eye-claro
track: T1-product-hero
packshot: assets/products/po-soft-eye-claro/01.png
duration_s: 12
```

## Documentos-chave

- [[brand-dna/00-brand-dna|Brand DNA]]
- [[tracks/README|Tracks]]
- [[pipeline/README|Pipeline V1]]
- [[pipeline/README-social-copy|Pipeline texto para social]]
- [[opensquad/squad.yaml|Squad OpenSquad]]
- [[_research/instagram/studio-formats|Formatos estúdio IG]]

## Status

- [x] Projeto + estrutura framework
- [x] Scrape catálogo + download 552 imagens
- [x] Brand DNA + tracks + pipeline docs + OpenSquad scaffold
- [x] Fichas DNA ricas por família/SKU (91 SKUs + families)
- [x] Fluxo de texto para social (copy) wired — 6 agentes (Vini/Theo/Bia/Duda/Cacá/Léa) + `pipeline_social_copy`
- [ ] Wiring Magnific + FFmpeg executável
- [ ] Primeiro golden path Soft Eye T1 renderizado
- [ ] Cast library V2 (fotos de modelo enviadas pelo cliente)
---
related:
  - "[[Clientes Ativos]]"
  - "[[00-inbox/instagram-lfpro.oficial/analise-comunicacao-lfpro|Análise IG LFPro]]"
  - "[[00-inbox/magnific-plano-premium-mais-mapa|Magnific créditos]]"
  - "[[00-inbox/magnific-kling-video-api|Magnific API vídeo]]"
---
