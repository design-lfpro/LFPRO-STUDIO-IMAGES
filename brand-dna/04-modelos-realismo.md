---
tags: [lfpro, brand-dna, casting, realismo, v2]
status: v2-draft
updated: 2026-08-10
decided_by: pendente aprovação Jonathan/Luciane
---

# Padrão de Modelo & Realismo — V2 (prep T4/T5)

Complementa `casting-v2.md`. Define **quem** pode ser modelo gerada/animada pela IA e **quanto** de fidelidade fotográfica é aceitável, para still e vídeo com pessoa (T4). T5 (before/after) continua bloqueado independentemente deste documento — ver `tracks/T5-face-proof/README.md`.

## 1. Padrão de elenco (persona)

| Critério | Regra V2 |
|---|---|
| Idade aparente | **30 anos ou mais** (mínimo). Sweet spot 32–50 — reforça "técnico-profissional aspiracional", evita o anti-pattern "teen e-girl makeup" já banido no Brand DNA |
| Tom de pele | Cobrir no mínimo os blocos de tom que a LF PRO já usa no shade range de produto: **claro / médio / médio-escuro / escuro**. Fitzpatrick aprox. I–VI representados no **elenco como um todo**, não numa modelo só |
| Nº mínimo de âncoras por tom | 1 modelo real (cast) por bloco de tom, reaproveitando de preferência modelo já contratada em campanha anterior (ver auditoria abaixo) |
| Gênero | Feminino como padrão (alinhado ao histórico de campanhas); modelo masculino só com pedido explícito no briefing |
| Postura de marca | "Profissional confiante" — não glam TikTok teen, não editorial extremo, não UGC banheiro |

### Por que 30+ e não a faixa de público (23–65)

O Brand DNA já separa **público de anúncio** (23–65, núcleo 25–45) de **quem representa a marca na tela**. A fundadora Luciane Ferraz — o rosto mais recorrente e mais bem recebido nos comentários (ver `_research/instagram/analise-comunicacao-lfpro.md`) — não é jovem, e a audiência responde a autoridade técnica, não a juventude. Fixar 30+ como piso de casting:

- Reforça "performance profissional" vs. "drugstore/glam teen" (ambos já nas regras invioláveis do `CLAUDE.md`)
- Evita o efeito "modelo genérica de banco de imagem" que IA tende a gerar por padrão (rosto ~22 anos, pele sem nenhuma linha de expressão)
- Não impede usar a Lu (fundadora) como âncora separada — ela já é ela mesma, sem limite de idade aplicável

## 2. Auditoria de material disponível (2026-08-10)

| Fonte | O que tem hoje | Uso possível |
|---|---|---|
| `assets/products/**` (site, 552 imgs) | Packshot puro, **zero pessoa** | Identity lock de produto — não serve de âncora de modelo |
| Instagram @lfpro.oficial (`_research/instagram/`) | Modelos diversas em tom de pele nos reels/posts (força #7 do relatório de comunicação); fundadora Lu recorrente; before/after com modelo (T5, fora de escopo) | Referência de estilo/pose/iluminação — não é âncora pixel-perfect (compressão do IG, direito de imagem de terceiros não claro) |
| Google Drive — Direcionais de campanha (2024–2025) | **Histórico real de casting**: cada lançamento contrata 3+ modelos, uma por bloco de tom (ex.: Jheniffer Ev/Claro, Ailime Trindade/Médio, Nikolly Alves/Escuro — Corretivo Mousse; Talita Hartmann, Alice Bobsim, Malu Brito — Batom; Breceane Costa, Samara, Bruna Jacobbi — Lápis). Contratação via agência (Contrato Direto, Container Casting, Fire Models), ~R$700–2.000/modelo | Melhor fonte para virar `assets/cast/{model_id}/` oficial — já é prática comercial validada pela marca |
| Google Drive — pasta modelo Soft Finish (`Soft Finish - Claro/Médio/Médio Escuro/Escuro - Model.png` + PSD) | Renders de still já aprovados por tom, ligados a arte final | Referência de enquadramento/still hero já validado pela marca |
| Google Drive — testes Magnific recentes (fora deste squad, últimos dias) | Arquivos como "movimento sutil da modelo" (i2v), "modelo sem acessórios", "a partir da img1 preservar…" | Prova de conceito manual já em andamento — precisa entrar no pipeline documentado, senão fica sem QC/lock e sem rastro de decisão |
| MAGNIFIC library (characters) | 1 único character salvo: `lu-golden` (projeto "SOCIAL MEDIA") | Provável âncora da fundadora; nenhum character de elenco diverso cadastrado ainda |
| `assets/cast/` (neste repo) | **Não existe ainda** | Criar seguindo `casting-v2.md`, uma pasta por `model_id` |

**Conclusão da auditoria:** a LF PRO já tem por prática contratar modelos cobrindo tom claro/médio/escuro a cada lançamento — a diversidade de pele pedida não é uma política nova, é a continuidade de um padrão real. O que falta é um **elenco fixo reaproveitável**: hoje cada campanha recontrata do zero. Recomendação: formalizar 2–4 dessas modelos já contratadas (uma por tom) como `assets/cast/{model_id}/` oficial, reaproveitando rosto real testado em vez de gerar modelo 100% sintética — o que já é regra em `casting-v2.md` ("não inventar modelo 100% IA como default se houver cast real").

## 3. Padrão de fidelidade de textura (still e vídeo)

| Elemento | Regra | Anti-pattern (banir no prompt) |
|---|---|---|
| Pele | Poros visíveis mas discretos, brilho especular natural (zona T), sem aspecto plástico | `airbrushed skin`, `beauty filter`, `poreless skin`, `waxy mannequin skin` (já banido no Brand DNA), `CGI skin`, `3D render skin` |
| Linhas de expressão | Suavizadas de forma **fotográfica** (retoque de still real de estúdio), nunca removidas por completo — especialmente onde o produto é um pó (Soft Eye/Soft Finish), cujo próprio acabamento soft-focus já justifica pele mais uniforme | `plastic surgery smooth`, `zero wrinkles digital paint-over` |
| Cabelo | Fio a fio real, brilho natural, sem aspecto de peruca | `wig-like hair`, `CGI hair strands`, `painted hair texture` |
| Maquiagem aplicada | Bem produzida, acabamento correto por produto (matte real do Soft Matte, soft-focus do Soft Eye/Finish, glow do Blend Cream) — descrito na ficha do SKU, nunca inventado | Acabamento genérico "IA glam" que não corresponde ao claim real do produto |
| Cor do produto na pele | Simulação de cor deve casar com o swatch real do packshot (`assets/products/{handle}/01.*`) e com o tom de pele real da modelo — mesma lógica de shade-match que já existe nos SKUs (6–13 tons por família) | Tom "médio" genérico que não corresponde a nenhum SKU real |
| Estilo geral | Sempre ultra-realista, foto de estúdio comercial | `illustration`, `cartoon`, `anime`, `3D render`, `plastic doll` |

### Ferramentas Magnific mapeadas (catálogo confirmado em 2026-08-10)

| Etapa | Ferramenta | Parâmetro recomendado |
|---|---|---|
| Still hero com modelo | `images_generate` com `references: [{type:"character", identifier:<cast_id>}, {type:"product", identifier:<packshot>}]` | Nano Banana Pro (`imagen-nano-banana-2`) — já é o still lock do V1; usar reference `character` para travar o rosto |
| Passo de realismo de pele (pós-still, opcional) | `images_skin_enhancer` | `version: faithful`, `skinDetail` moderado (30–50; 100 tende a "vidro"). **Nunca** `optimizedFor: no_make_up` — removeria a maquiagem, que é o produto sendo vendido |
| Upscale final | `images_upscale` | `mode: ultra-photo` ou `precision` com `optimised: SoftPortrait` (peles mais claras) / `HardPortrait` (peles mais escuras, mais contraste). Evitar `mode: creative` com preset `wild` — hallucina textura de pele |
| Vídeo i2v com rosto | `video_generate` com `references: [{type:"character", identifier:<cast_id>}]` + `keyframes.start/end` | **Seedance 2.0** (`bytedance-seedance-pro-2.0`) — tier `sota`, recomendado explicitamente para `realistic_videos` + `reference_guided` com `character`; Kling 3.0 (lock atual de produto T1/T2) não expõe reference `character` no catálogo, então não serve para travar rosto entre frames |
| Gate antes do vídeo | Novo agente `Nina Pele` (`opensquad/agents/nina-pele.agent.md`) | Roda como a Rita Still Verifier, mas para pessoa: identidade, pele, cor de produto |

> Nota: `brand-dna/01-modelos-magnific.md` trava Kling 3.0 / Nano Banana para **produto sem rosto (T1/T2)**. Este documento não altera aquele lock — define o motor **adicional** exigido por T4 (com rosto), que precisa de reference `character`, capacidade ausente no catálogo atual do Kling 3.0.

## 4. Direito de imagem e uso por IA

Contratos antigos (Drive, 2024–2025) foram fechados para **still/vídeo convencional de uma campanha**, não necessariamente para **reuso via geração de IA** (variação de ângulo, animação i2v, reaproveitamento entre campanhas). Antes de promover qualquer modelo do histórico para `assets/cast/`:

1. Confirmar com jurídico/booker se o contrato original cobre "geração e manipulação por inteligência artificial"
2. Se não cobrir, tratar como **novo uso** → aditivo de contrato ou nova sessão já ciente do uso em IA
3. Documentar em `assets/cast/{model_id}/meta.yaml` no campo `consent_ai_use: true|false`

## 5. Status

- [ ] Aprovação do piso de idade (30+) por Jonathan/Luciane
- [ ] Escolher 2–4 modelos do histórico para virar `assets/cast/` oficial (uma por tom)
- [ ] Confirmar direito de uso por IA dos contratos antigos
- [ ] Cadastrar characters no Magnific library (hoje só existe `lu-golden`)
- [ ] Trazer os testes manuais recentes do Drive ("movimento sutil da modelo" etc.) para dentro do pipeline documentado, com QC da Nina Pele
