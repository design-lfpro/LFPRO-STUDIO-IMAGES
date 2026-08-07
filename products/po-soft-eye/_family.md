---
family: po-soft-eye
title: "Linha Pó Soft Eye"
product_type: Pó
handles: [po-soft-eye-claro, po-soft-eye-medio, po-soft-eye-escuro]
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
status: dna-v1
hero_claim_brand: "Associado ao 'pó mais viralizado na internet' — usar só em comunicação Soft Eye"
updated: 2026-08-06
---

# Família Soft Eye — DNA compartilhado

## Identidade

Pó solto para região dos olhos / finalização com efeito soft focus. Embalagem **icone** da marca no e-commerce: pote com sifter dourado, tampa preta monograma gold, puff preta com fita.

## Packaging lock (NUNCA redesenhar)

Observado nos packshots oficiais (`01.png` de cada tom):

### Componentes

1. **Tampa (lid)**  
   - Disco preto brilhante/liso  
   - **Monograma LF dourado** grande, central, levemente em relevo/foil  
   - Wordmark **LF PRO** em gold, tipografia fina, alinhada ao monograma (no packshot da tampa aberta, o monograma fica de cabeça para o observador em alguns ângulos — preservar como na foto ref)

2. **Anel / sifter dourado**  
   - Disco metalizado dourado com **grade de furos circulares** regulares (sifter)  
   - Borda dourada espelhada  
   - Furos limpos, não ovalizar nem fundir

3. **Base do pote**  
   - Corpo cilíndrico **translúcido / fosco claro** (não vidro cristal grosso escuro)  
   - Parede fina; interior mostra pó

4. **Puff**  
   - Redonda, veludo/microfiber **preto**  
   - Fita preta diametral com monograma LF + texto `LF PRO` em gold  
   - Costura/acabamento limpo

5. **Pó / swatch**  
   - Mancha de pó solto no fundo da composição (site)  
   - Textura pulverulenta, borda irregular natural  
   - Cor varia por tom (ver SKU)

### Fotografia site (gramática)

- Fundo: off-white seamless  
- Composição típica: tampa semi-aberta + pote + puff à esquerda + swatch de pó à direita/baixo  
- Sombra soft única sob o grupo  
- High-key beauty ecommerce, sem props

## Cores de packaging (fixas)

| Elemento | Hex aprox |
|----------|-----------|
| Tampa preta | `#0A0A0A`–`#121212` |
| Gold logo / sifter | `#C9A227`–`#E1C46A` (highlights mais claros) |
| Corpo pote | `#EDE8E2` translúcido |
| Puff | `#0A0A0A` |
| Fundo site | `#F7F5F2` |

## Prompt anchors (EN) — família

### Still lock (identity)

```
Exact product packaging match to reference photo: LF PRO Soft Eye loose powder,
glossy black circular lid with precise gold LF monogram logo and LF PRO lettering,
gold metallic sifter disc with clean circular perforation holes,
translucent matte jar body, black velvet puff with black ribbon and gold LF PRO print,
premium beauty ecommerce lighting, preserve logo sharpness, no redesign
```

### Studio hero T1 (dark feed)

```
Same exact Soft Eye powder packaging as reference, product hero on dark charcoal seamless background #0E0E0E,
soft beauty key light + subtle gold rim, micro push-in, 9:16 commercial,
logo and sifter holes perfectly preserved, no hands, no face
```

### Texture macro T2

```
Extreme macro of fine loose face powder texture matching reference swatch color,
soft-focus silky particles, premium beauty, shallow depth of field,
optional soft powder dust drift, no face, packaging only if partial in frame with correct gold black design
```

## Anti-patterns família

- Sifter sem furos ou furos bagunçados  
- Logo prata / branco  
- Puff rosa ou sem fita  
- Pote de vidro âmbar genérico  
- Aplicar pó em olho full-face (T5)

## Notas pipeline V1

- Golden path recomendado: `po-soft-eye-claro` T1 12s  
- Usar `01.png` como reference obrigatória  
- Imagens 02+ do site costumam reforçar ângulos/swatch — usar em storyboard  
