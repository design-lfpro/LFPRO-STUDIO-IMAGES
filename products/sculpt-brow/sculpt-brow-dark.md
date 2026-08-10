---
handle: sculpt-brow-dark
title: "Sculpt Brow Dark"
family: sculpt-brow
product_type: "Lapiseira retrátil de sobrancelha"
url: "pendente — produto ainda não lançado no site (previsto 13/08)"
preferred_tracks: [T1-product-hero, T2-texture-macro, T4-model-portrait]
blocked_tracks: [T5-face-proof]
status: dna-v1-pending-launch
assets_local: "assets/products/sculpt-brow-dark/01.png (packshot isolado, fundo off-white)"
shade: Dark
pencil_hex_approx: "#3B2A24"
---

# Sculpt Brow Dark

## Identidade do produto

Lapiseira retrátil de sobrancelha tom **Dark** — marrom profundo acinzentado, subtom frio. Mesma embalagem da família; diferencia-se pela cor do grafite/ponta.

- Handle previsto: `sculpt-brow-dark` (a confirmar contra o site após o lançamento de 13/08)
- Indicação oficial: fios castanho escuro, pretos e de alto contraste

## Packaging (lock visual)

Idêntico ao [[_family|DNA da família Sculpt Brow]]: corpo preto brilhante, wordmark "SCULPT BROW" gold, monograma LF gold, tampa que remodela a ponta chanfrada. **Não alterar** nenhum destes elementos entre tons.

## Cast vinculado

`assets/cast/sculpt-brow-modelo-dark/` — modelo IA (ver `meta.yaml`, aprovada para esta campanha em 2026-08-10).

## Claims oficiais

Ver claims completos da família em `_family.md` — o Dark não tem claim exclusivo além do tom/indicação de uso.

## Notas para pipeline

- Packshot isolado confirmado (2026-08-10, Drive → `FOTO PRODUTO/SITE` do Sculpt Brow): `assets/products/sculpt-brow-dark/01.png` — caneta aberta + tampa separada, fundo off-white, ponta chanfrada marrom profundo/acinzentado visível, wordmark e monograma gold nítidos. **Usar este como reference obrigatória de still-lock (T1/T4)**, não mais o flat-lay de família.
- Existe também detalhe de ponta (`SCULPT BROW DARK CHANFRADO.png`) e swatch de aplicação (`SCULPT BROW SWAT PRODUTO bege dark.png`) no Drive, ainda não importados — trazer se for fazer T2 (macro) ou conferência de shade-match.
- Cor de grafite exata (`#3B2A24`) é estimativa a partir do flat-lay — recalibrar direto no packshot isolado antes de still-lock final.
