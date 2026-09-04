# CLAUDE.md — LFPro Studio

Contexto para agentes trabalhando neste projeto. Cliente: **LF PRO** (maquiagem & skincare). Projeto de fábrica de vídeo de produto com IA.

## O que é

Framework + squad OpenSquad para gerar vídeos de **estúdio product-hero** a partir de packshots oficiais.  
**V1 ativa:** tracks T1 (product hero) e T2 (texture macro).  
**V2 planejada:** T4 model portrait com âncoras fotográficas do cliente.  
**V3 planejada:** T5 face-proof (before/after) — portão fechado.

## Regras invioláveis

1. **Nunca redesenhar packaging.** Logo LF monogram dourado, tipografia do tubo/pote, pump gold, sifter, etc. vêm do packshot real (`assets/products/{handle}/01.*`).
2. **Não inventar claims.** Só claims do `body_text` do site ou da ficha do produto.
3. **Não gerar full-face makeup proof no V1.** Tracks T5 bloqueados.
4. **Produto = ficha**, não squad. Um squad `lfpro-studio`, N fichas.
5. **Magnific** é o motor de geração (não kie.ai neste projeto).
6. **Modelos LOCK V1:** stills = **Google Nano Banana** (`imagen-nano-banana-2` @ 2k); vídeo = **flexível entre os dois melhores custo-benefício** — **Kling 3.0** (`kling-30`) ou **Seedance 2.0** (`bytedance-seedance-pro-2.0`), 720p, escolha por run. **Proibido:** Seedance 1.5 (Draft ou não) — reprovado em A/B por qualidade. Ver `brand-dna/01-modelos-magnific.md`.
7. **FFmpeg** fecha master 9:16; IA gera clipes atômicos 4–8s.
8. Responder em **PT-BR**; prompts de imagem/vídeo em **EN**.

## Onde está o quê

| Path | Uso |
|------|-----|
| `brand-dna/` | Leis globais da marca + `01-modelos-magnific.md` (Nano Banana + Seedance) |
| `products/{family}/` | `_family.md` + `{handle}.md` |
| `tracks/T*/` | Spec do track |
| `pipeline/` | Steps V1, scripts |
| `opensquad/` | Squad pronto para copiar p/ `/home/projects/opensquad/squads/lfpro-studio` |
| `assets/products/{handle}/` | Imagens oficiais do site |
| `assets/catalog/` | JSON catálogo |

## Input canônico de um run V1

```yaml
handle: po-soft-eye-claro          # obrigatório
track: T1-product-hero             # T1 | T2
duration_s: 12                     # default 12
aspect: "9:16"
packshot: auto                     # resolve assets/products/{handle}/01.*
style_override: null               # opcional: dark-feed | white-ecommerce
```

## Dois sistemas fotográficos da marca

1. **Ecommerce (site):** fundo off-white `#F7F5F2`–`#FAFAF8`, sombra soft, packshot 3/4, frequentemente + swatch.  
2. **Feed/estúdio dark (IG):** preto + dourado + nude, luz dramática, product float.

V1 deve aceitar os dois via `style_override`. Default de vídeo social: **dark-feed**. Default de still identity lock: **sempre packshot do site**.

## Logo lock (observado nos packshots)

- Monograma **LF** estilizado em **dourado** (gold foil look)
- Wordmark **LF PRO** em gold, muitas vezes vertical no cabo de pincéis ou sob monograma na tampa
- Embalagens core: **preto fosco/brilhante + ouro**
- Nunca inventar logo alternativo, never “LFPro” sem espaço se o packaging usa “LF PRO”

## Ordem de leitura para qualquer agente

1. Este CLAUDE.md  
2. `brand-dna/00-brand-dna.md`  
3. Ficha `products/.../{handle}.md` (+ `_family.md`)  
4. Track `tracks/T*/README.md`  
5. Pipeline step atual  

## Relacionados no vault

- Gestor / Luci / Tráfego LFPro em `01-projetos/`
- Análise IG: `00-inbox/instagram-lfpro.oficial/`
- Magnific: `00-inbox/magnific-*`
- OpenSquad VPS: `/home/projects/opensquad` (squads edit-videos, vox-collage, vox-cenas como referência de pipeline)
