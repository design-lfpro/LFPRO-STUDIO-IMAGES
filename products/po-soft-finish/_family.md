---
family: po-soft-finish
handles: ['po-soft-finish-cor-medio-claro', 'po-soft-finish-medio-escuro', 'po-soft-finish-claro', 'po-soft-finish-medio', 'po-soft-finish-escuro']
preferred_tracks: [T1-product-hero]
blocked_tracks: [T5-face-proof]
status: dna-v1-scaffold
updated: 2026-08-06
---

# Família `po-soft-finish`

## Packaging lock (base)

See packshot

**Fonte da verdade:** `assets/products/{handle}/01.*` de cada SKU.  
Detalhamento fino por imagem deve enriquecer esta ficha (passada vision).

## Packaging confirmado pela cliente

- **Pote todo preto** (base opaca preta + tampa preta), peneira dourada perfurada; o pó NÃO aparece pela lateral.
- Tampa: monograma LF dourado + "LF PRO". **Nenhum texto na lateral do pote** (nem "SOFT FINISH", nem nome da cor).
- Prompt anchor: "fully black opaque jar, black base and black lid, no text on the side".

## Prompt anchor família (EN)

```
exact product from reference, match reference photo 1:1, preserve LF PRO gold black branding, no redesign
```

## Anti-patterns

- Logo errado, packaging genérico, tom/cor de produto errado, full-face T5
