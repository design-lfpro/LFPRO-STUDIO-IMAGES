---
handle: po-soft-eye-escuro
title: "Pó Soft Eye Escuro"
family: po-soft-eye
product_type: "Pó"
url: "https://lfpro.com.br/products/po-soft-eye-escuro"
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
status: dna-v1
assets_local: assets/products/po-soft-eye-escuro/
shade: Escuro
powder_hex_approx: "#C4A07A"
---

# Pó Soft Eye Escuro

## Identidade do produto

Pó Soft Eye tom **Escuro**. Mesma embalagem da família; diferencia-se pela **cor do pó** no pote e no swatch.

- Handle Shopify: `po-soft-eye-escuro`
- URL: https://lfpro.com.br/products/po-soft-eye-escuro
- Imagens locais: 01.png, 02.png, 03.png, 04.png, 05.png, 06.png, 07.png, 08.png, 09.png

## Packaging (lock visual)

Idêntico ao [[_family|DNA da família Soft Eye]]:

- Tampa preta + monograma LF gold + LF PRO
- Sifter dourado perfurado
- Pote translúcido
- Puff preta com fita gold brand
- **Não alterar** nenhum destes elementos entre tons

## Cores e materiais

| Elemento | Spec |
|----------|------|
| Packaging | ver family |
| Pó / swatch | bege-escuro / tan para peles mais profundas (`#C4A07A` aprox) |
| Nota | não clarear para ivory na geração |

## Logo e tipografia no produto

Monograma LF + LF PRO em gold na tampa e na fita da puff. Sem texto de tom na tampa (tom vem da cor do pó / naming).

## Textura / fórmula visível

Pó solto fino, acabamento pulverulento no swatch do site. Macro T2 deve parecer **soft silk powder**, não glitter e não areia grossa.

## Fotografia de estúdio do site

High-key off-white; composição aberta (tampa + pote + puff + swatch). Para vídeo social: re-iluminar em **dark-feed** mantendo o mesmo objeto.

## Diferenças vs outros tons da linha

| Tom | Handle | Pó (aprox) |
|-----|--------|------------|
| Claro | po-soft-eye-claro | ivory/peach claro |
| Médio | po-soft-eye-medio | bege médio |
| Escuro | po-soft-eye-escuro | bege-escuro |

Este SKU = **Escuro**. Não misturar cor de pó de outro handle.

## Prompt anchors (EN)

### Still lock (packshot identity)

```
Exact LF PRO Soft Eye loose powder shade Escuro, match reference image packaging 1:1,
black lid gold LF monogram, gold perforated sifter, translucent jar filled with bege-escuro / tan para peles mais profundas,
black puff with gold LF PRO ribbon, powder swatch color #C4A07A,
ecommerce white background, preserve logo, no redesign
```

### Studio hero scene (T1)

```
LF PRO Soft Eye Escuro exact packaging from reference on dark charcoal beauty studio backdrop,
soft key + gold rim light, product hero 3/4, micro push-in, 9:16,
powder color #C4A07A visible if open, logo sharp, no face no hands
```

### Texture macro (T2)

```
Macro silky loose powder texture color #C4A07A, fine soft particles, premium beauty soft focus,
gentle dust motes, shallow DOF, no face
```

## Anti-patterns

- Trocar tom do pó
- Deformar sifter/logo
- Full-face application (T5)
- Embalagem de outra marca “inspired”

## Claims oficiais (site)

> O Soft Eye LF PRO é o pó solto de acabamento que une leveza, tecnologia e elegância em uma única fórmula. Com textura ultrafina e toque sedoso, ele sela a maquiagem, uniformiza a pele e proporciona um efeito soft focus , que suaviza linhas, controla o brilho e revela uma aparência naturalmente iluminada. Mais do que um pó, o Soft Eye é o que transforma sua maquiagem em uma experiência sensorial: conforto absoluto, acabamento profissional e pele com aspecto sofisticado durante todo o dia. O que torna o Soft Eye único Textura ultrafina e leve: cria uma camada imperceptível que não bloqueia a luz, mantendo a pele com viço e aspecto natural. Acabamento soft focus: disfarça linhas e imperfeições, oferecendo efeito aveludado e uniforme. Fórmula adaptável: com baixa pigmentação, se ajusta perfeitamente a diferentes tons de pele, disponível nas cores clara, média e escura. Uso versátil: ideal para todo o rosto e todos os tipos de pele, inclusive as maduras. Durabilidade e conforto: controla a oleosidade e mantém o acabamento impecável ao longo do dia, sem ressecar. Diferenciais de aplicação Acompanha uma esponja macia e aveludada, que se encaixa perfeitamente à embalagem e garante uma aplicação precisa, confortável e sem desperdício.

## Notas para pipeline V1

- Reference obrigatória: `assets/products/po-soft-eye-escuro/01.png` (ou extensão local)
- Golden path marca: preferir **claro** para demos se não especificado
- Composite dark: extrair produto do fundo branco e colocar em #0E0E0E
