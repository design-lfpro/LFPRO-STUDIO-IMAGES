---
tags: [lfpro-studio, magnific, multi-product, fidelidade]
status: v1-addendum
updated: 2026-08-25
decided_by: sessão de geração social (fidelidade de embalagem)
---

# Multi-Product Lineup — regras de fidelidade (addendum V1)

Sofia, Gael e Rita foram desenhadas para still de **1 SKU por vez** (par start/end, T1/T2). Este documento cobre o caso que não tinha protocolo: **hero/flat-lay social com N produtos LF PRO na mesma cena** (ex: "vitrine da marca", lineup estilo editorial). Nasceu de erros reais e repetidos — deformação de logo, ponta de lápis errada, escala trocada, pincel redesenhado — em cenas com 7–10 produtos simultâneos.

> Regra de ouro: **cada chamada de `images_generate` é uma geração nova do zero, nunca uma edição.** Pedir "mantém o resto igual" no prompt não trava pixel nenhum — é só um pedido de texto que o modelo pode ignorar. Itens já aprovados numa rodada podem voltar a variar na próxima. Trate cada rodada como um novo rolo de dados, não como um ajuste incremental.

## 1. Cap de produtos simultâneos

| Produtos na cena | Risco de fidelidade |
|---|---|
| 1–3 | Baixo — reference forte, alta chance de fidelidade 1:1 |
| 4–5 | Moderado — recomendado, é o teto confortável |
| 6 | Máximo tolerável — só com prompt enxuto, sem instruções corretivas empilhadas |
| 7–10 | **Alto risco observado** — múltiplas deformações simultâneas mesmo com reference photo por item |

**Regra:** default ≤5 produtos por chamada. Acima de 6, dividir em 2+ composições e montar depois (colagem manual ou 2 hero shots do mesmo lineup), ou aceitar risco maior e reservar orçamento pra 2–3 rodadas de correção.

## 2. Reference por item

- Sempre o packshot oficial completo (`assets/products/{handle}/01.*`) — nunca text-only.
- Para **detalhe pequeno crítico** (ponta de lápis, gravação de pincel, logo em objeto pequeno no frame): além do packshot completo, gerar um **close-up crop dedicado** (`images_crop` com `auto:true`, aspect que enquadre só o detalhe, prompt tipo "extreme close-up filling the whole frame with just X, nothing else visible"). Passar os dois — packshot completo + crop — como references separadas.
- Cuidado: `images_crop` com `auto:true` é ele mesmo generativo (custa ~40cr, tool interno = `expand`) — não é um crop pixel-perfeito garantido. Serve pra dar mais peso visual ao detalhe, não é fonte de verdade absoluta.

## 3. Instruções de escala — regra crítica

- **Sempre auto-referencial:** "reduza ~20% mantendo forma/cor/gravação idênticas à reference" — nunca peça pro modelo comparar o tamanho de um item com outro de **categoria/forma diferente** (ex: "o pincel deve ficar do tamanho do tubo de base"). Isso já causou o modelo **redesenhar o objeto inteiro** (pincel virou outra coisa) na tentativa de reconciliar formas incompatíveis.
- Comparação entre itens da **mesma categoria/forma** é segura (ex: "tubo de base e tubo de primer do mesmo tamanho entre si" — os dois são tubos, funcionou).
- Evite linguagem de "reflexo"/"espelhado" em objetos flat (paletas, compactos) — observado causar artefato visual estranho na superfície. Prefira "acabamento fosco com leve brilho sutil".

## 4. Correção de composição já aprovada — NÃO regenerar tudo de novo

Se uma rodada já teve itens aprovados e só 1–2 elementos precisam de ajuste:

1. **Preferir `images_retouch`** (mask branco = mudar, preto = mantém) sobre a região específica — isso sim preserva pixel do resto.
2. A máscara precisa ser desenhada olhando a imagem — normalmente feito pelo humano no app da Magnific (Claude não tem acesso visual ao render nesta sessão). Preparar o prompt de texto por região com antecedência pra agilizar.
3. **Nunca** propor "mais um full-regenerate com prompt ajustado" como primeira opção depois de uma composição já aprovada — isso já causou regressão total (itens aprovados voltaram a ficar errados) mais de uma vez nesta sessão.

## 5. Escalada (2 tentativas e muda de estratégia)

- Mesma regra do gate padrão (`01-modelos-magnific.md`): **máx 2 re-rolls** no mesmo elemento.
- Depois de 2 falhas seguidas no mesmo item: parar de tentar `images_generate` de novo pra esse elemento. Migrar pra:
  - `images_retouch` mascarado (item 4), ou
  - Composite manual do packshot real por cima (overlay), preferível quando o logo é o problema.

## 6. QC multi-produto (Rita)

Pra cena com N produtos, Rita usa checklist **PASS/FAIL por produto**, não só por frame — ver `opensquad/agents/rita-still-verifier.agent.md`. Sem esse checklist estruturado, é fácil aprovar uma cena com 1 produto quebrado que passou despercebido no meio dos outros 9.
