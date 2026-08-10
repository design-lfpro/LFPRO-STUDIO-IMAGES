---
family: sculpt-brow
title: "Sculpt Brow — Lapiseira Retrátil para Sobrancelhas"
product_type: "Lapiseira retrátil de sobrancelha"
handles: [sculpt-brow-light, sculpt-brow-medium, sculpt-brow-dark]
preferred_tracks: [T1-product-hero, T2-texture-macro, T4-model-portrait]
blocked_tracks: [T5-face-proof]
status: dna-v1-pending-launch
launch_note: "Lançamento previsto 13/08 (pasta Drive '0813 - SCULPT BROW LANÇAMENTO'). Produto ainda não está no scrape do site (assets/catalog/) — não confundir com os 91 SKUs já catalogados."
updated: 2026-08-10
---

# Família Sculpt Brow — DNA compartilhado

## Identidade

Lapiseira retrátil de sobrancelha com ponta chanfrada dupla função (fio a fio fino / preenchimento rápido). Formato slim, corpo **preto brilhante**, wordmark **"SCULPT BROW"** em gold, monograma **LF** gold na base. Vem em **3 tons estratégicos**: Light, Medium, Dark.

## Packaging lock (NUNCA redesenhar)

Observado nos packshots reais (Drive, pré-lançamento — ainda não há `01.png` isolado por tom, ver nota em §Assets):

1. **Corpo** — cilindro preto brilhante/laqueado, slim, tipo lapiseira
2. **Wordmark** — `SCULPT BROW` em gold, caixa alta, ao longo do corpo
3. **Monograma LF** — gold, próximo à base/tampa
4. **Tampa** — mesma laca preta, encaixe por fricção, pode ser usada para remodelar a ponta chanfrada (pressionar contra superfície plana)
5. **Ponta** — grafite chanfrado, cor varia por tom (marrom claro/médio/profundo acinzentado — sempre subtom frio)

### Fotografia (gramática observada)

- Fundo bege/nude quente (mais próximo do "feed dark/vanity" que do off-white puro de ecommerce — calibrar com `brand-dna/00-brand-dna.md §2` antes do golden path)
- Composição flat-lay com múltiplas unidades em ângulos cruzados, tampas soltas, foco na ponta chanfrada
- Luz suave, sem props além do próprio produto

## Cores de packaging (fixas)

| Elemento | Hex aprox |
|----------|-----------|
| Corpo/tampa preto | `#0A0A0A`–`#121212` |
| Wordmark/monograma gold | `#C9A227`–`#D4AF37` |
| Fundo packshot (Drive) | bege nude quente, aprox `#D9BFA0`–`#E6D2B8` (medir no still real antes de travar hex) |

## Três tons estratégicos (claim oficial)

| Tom | Handle | Descrição oficial | Indicação |
|-----|--------|--------------------|-----------|
| **Light** | `sculpt-brow-light` | Marrom claro, subtom frio | Fios loiros, castanho claro, ruivos, baixo contraste |
| **Medium** | `sculpt-brow-medium` | Marrom médio, subtom frio | Fios castanho médio, morenos, médio contraste |
| **Dark** | `sculpt-brow-dark` | Marrom profundo acinzentado, subtom frio | Fios castanho escuro, pretos, alto contraste |

## Claims oficiais (fonte: `sculpt brow.pdf`, dizeres/copy de lançamento — Drive)

> Sobrancelhas definidas com efeito natural. Uma lapiseira retrátil desenvolvida para criar sobrancelhas naturalmente definidas. Sua ponta chanfrada permite desenhar fios ultrafinos ou preencher falhas com rapidez, proporcionando um resultado preciso, elegante e profissional. Uma ponta, duas funções: use a extremidade fina para desenhar fios ultrafinos ou a face mais ampla para preencher falhas com rapidez e naturalidade. Formato impecável: após o uso, basta pressionar suavemente a ponta contra uma superfície plana para remodelar o formato chanfrado. Efeito fio a fio, acabamento natural, definição precisa, preenchimento uniforme, resultado rápido, acabamento profissional. Alta performance: super macia, desliza facilmente, não puxa os fios, esfuma com facilidade, resistente à água, resistente à oleosidade, não transfere, acabamento matte natural. Enriquecida com ativos que ajudam a cuidar dos fios durante o uso — Óleo de Mamona (hidrata e promove maciez) e Vitamina E (ação antioxidante e proteção). Fórmula anidra, clean beauty: 100% vegana, sem fragrância, sem água, sem conservantes.

## Anti-patterns família

- Trocar o gold do wordmark/monograma por prata ou branco
- Ponta chanfrada arredondada/lápis comum (perde o diferencial "uma ponta, duas funções")
- Cor de grafite que não corresponde ao tom do handle
- Full-face brow makeover / antes-depois de sobrancelha completa (T5)

## Assets — status (2026-08-10)

- `assets/products/sculpt-brow/01.png`, `02.png`: packshot de **família** (flat-lay com as 3 unidades) — bom para still de família/carrossel, não para still-lock de handle individual.
- `assets/products/sculpt-brow-{light,medium,dark}/01.png`: **packshot isolado por tom**, trazido do Drive (pasta `FOTO PRODUTO/SITE` do Sculpt Brow) — caneta aberta + tampa separada, fundo off-white, ponta chanfrada na cor certa do tom. **Esta é a reference obrigatória de still-lock por handle a partir de agora.**
- No Drive existem ainda, não importados: detalhe de ponta chanfrada por tom (`SCULPT BROW {LIGHT,MEDIUM,DARK} CHANFRADO.png` — bom pra T2 macro) e swatch de aplicação em pele (`SCULPT BROW SWAT PRODUTO bege {light,medium,dark}.png` — bom pra conferência de shade-match). Trazer quando o track exigir.
- Cast de modelo vinculado: ver `assets/cast/sculpt-brow-modelo-{light,medium,dark}/` (já com `magnific_character_id` preenchido).

## Notas pipeline V1/V2

- Golden path ainda não definido — produto pré-lançamento, sem histórico de golden path. Com packshot isolado + cast + character já linkados, T1 e T4 estão desbloqueados tecnicamente para o Sculpt Brow.
- Para still de família/carrossel: pode seguir com `packshot-composite` a partir do flat-lay. Para still por tom (T1/T4): usar sempre o `01.png` isolado do handle correspondente como reference — nunca gerar packaging do zero por IA sem reference.
