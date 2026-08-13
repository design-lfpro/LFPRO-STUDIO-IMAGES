---
family: essential-lips
product_type: Batom Líquido Matte
handles_oficiais_linha: ['essential-lips-beige', 'essential-lips-blush', 'essential-lips-carmim', 'essential-lips-clay', 'essential-lips-malt', 'essential-lips-mauve', 'essential-lips-rose', 'essential-lips-wine']
handles_campanha_v1: ['essential-lips-rose', 'essential-lips-carmim', 'essential-lips-wine']
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
status: dna-v1-scaffold
updated: 2026-08-13
---

# Família `essential-lips`

Produto novo (ainda não publicado no site / não está em `assets/catalog`). Fonte dos dados: Google Drive (pastas "Essential Lips - Batom Líquido" e "ESSENTIAL LIPS 🫟" — adesivos e cartuchos das 8 tonalidades já fechados em arte).

## Tonalidades da linha

A linha completa tem **8 tons oficiais** (adesivo + cartucho já produzidos): `Beige`, `Blush`, `Carmim`, `Clay`, `Malt`, `Mauve`, `Rose`, `Wine`.

**Trio da campanha V1 (escolhido em briefing):** `Rose`, `Carmim`, `Wine`.

## Packaging lock (base)

Visto na foto de referência enviada em briefing (frasco + cartucho físico, sem tom de cor identificado — usar só como trava de embalagem, não como packshot de um handle específico):

- Tampa preta glossy, cilíndrica, alta
- Frasco/corpo transparente/fosco deixando ver o líquido colorido por dentro
- Monograma **LF** dourado + wordmark **LF PRO** dourada aplicados no corpo do frasco
- Cartucho preto fosco, wordmark **"ESSENTIAL LIPS"** dourada vertical + "Batom Líquido 4,5ml" menor
- **Fonte da verdade definitiva:** ainda não há packshot oficial por tom em `assets/products/{handle}/01.*` — as pastas do Drive "FOTO PRODUTO" (criadas 12/08) estão vazias. Não gerar still de still-lock (T1) até esse asset chegar.

## Prompt anchor família (EN) — provisório, revisar quando packshot oficial chegar

```
exact LF PRO Essential Lips liquid matte lipstick packaging from reference, glossy black cap, clear/frosted barrel showing colored liquid, gold LF monogram and gold "LF PRO" wordmark, black carton with gold "ESSENTIAL LIPS" vertical wordmark, match reference photo 1:1, preserve LF PRO gold black branding, no redesign
```

## Claims

**Nenhum claim de venda oficial encontrado ainda** (só achei o docx "Dizeres de Rotulagem" com INCI/regulatório, sem copy de venda). Não inventar claims — aguardar copy oficial do time de marketing antes de escrever fichas por handle.

## Anti-patterns

- Logo errado, packaging genérico, tom/cor de produto errado, full-face T5
- Não tratar a foto de referência do briefing como packshot definitivo de um tom específico
- Não gerar still-lock (T1 still de identidade) sem packshot oficial por handle

## Notas para pipeline V1

- Ficha por handle (`essential-lips-rose.md` etc.) ainda não criada — depende de packshot oficial + claims oficiais
- Casting da campanha (trio de modelos por tom de pele): ver [[_casting]]
