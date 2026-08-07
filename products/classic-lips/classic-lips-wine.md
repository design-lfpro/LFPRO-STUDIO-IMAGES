---
handle: classic-lips-wine
title: Classic Lips Wine
family: classic-lips
product_type: Batom
sku: "12704"
price: "69.90"
url: https://lfpro.com.br/products/classic-lips-wine
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
status: dna-v1
assets_local: assets/products/classic-lips-wine/
shade: Wine
---

# Classic Lips Wine

## Identidade do produto

Batom Classic Lips tom **Wine**. Mesmo packaging black+gold da linha; diferencial exclusivo = cor da bala **Vinho / burgundy deep berry, vermelho-roxo escuro sofisticado** (hex aprox. `#7A1F3D / #6B1834`).

## Packaging (lock visual)

Ver [[_family|Classic Lips DNA]]. Lock pixel-level:

1. Cap preto glossy à esquerda: monograma LF dourado grande + “LF PRO” dourado abaixo; aro gold no topo
2. Stick aberto à direita: base preta + coluna gold mirror + bullet na cor Wine com monograma LF embutido no topo
3. Sem texto de tom no pack
4. Proporção e composição 01: cap ~mesmo altura do stick fechado visual; bullet exposto ~1/3 superior

**Assets:** `assets/products/classic-lips-wine/01.webp` (hero), `02.png` (macro texture quando existir), `03+` on-lips/swatch.

## Cores e materiais

| Parte | Cor / hex aprox |
|-------|-----------------|
| Cap / base | Preto glossy `#0A0A0A` |
| Aro + coluna | Ouro `#C9A227`–`#D4AF37` |
| Bullet Wine | #7A1F3D / #6B1834 |
| Fundo site | Off-white `#F7F5F2` |

## Logo e tipografia no produto

- Cap: monograma **LF** gold foil + wordmark **LF PRO** gold uppercase
- Bullet: monograma LF em relevo na própria cera (cor do tom)
- Não alterar tipografia nem proporção do monograma

## Textura / fórmula visível

- Bullet: cremoso satin, superfície lisa com leve sheen de óleos
- Macro (02 se houver): smear da mesma cor, espesso, pigmentado, sem glitter grosso
- On-lips referência: cobertura uniforme, satinado, sem craquelar

## Fotografia de estúdio do site

- Fundo seamless off-white, soft key light frontal-superior
- Sombra de contato sutil sob cap e stick
- Ângulo leve 3/4 frontal; sem mão, sem props
- Composição fixa família: cap left, open stick right

## Diferenças vs outros tons da linha

Tom mais escuro da linha. Alto impacto em fundo claro e dark-feed. Não confundir com Carmim (Carmim é true red).

## Prompt anchors (EN)

### Still lock (packshot identity)
```
Exact LF PRO Classic Lips Wine lipstick packshot. Glossy black cap with gold LF monogram and gold "LF PRO" text, thin gold top rim. Open gold metallic barrel, black base. Creamy lipstick bullet shade Vinho / burgundy deep berry, vermelho-roxo escuro sofisticado, color approx #7A1F3D / #6B1834, embossed LF monogram on bullet tip. Off-white #F7F5F2 background, soft studio light, soft shadow. Photorealistic e-commerce, identity lock, do not redesign packaging.
```

### Studio hero scene (T1)
```
9:16 luxury product hero. Classic Lips Wine (#7A1F3D / #6B1834) on deep black background with subtle gold accent light. Black glossy cap and gold barrel identity locked. Slow elegant float/orbit, specular highlights on gold metal, creamy Wine bullet visible. Premium cosmetics commercial, cinematic.
```

### Texture macro (T2)
```
Macro beauty shot: Classic Lips Wine bullet tip with embossed LF logo, gold collar below. Background thick creamy smear of same shade #7A1F3D / #6B1834. Buttery hydrating lipstick texture, rich pigment, soft sheen, no matte powder look. Photorealistic texture advertising.
```

## Anti-patterns

- Não mudar a cor do bullet para outro tom da linha
- Não packaging matte / prata / branco
- Não remover monograma LF do cap ou do bullet
- Não gerar gloss tube / liquid lipstick
- Não full-face (T5 bloqueado)
- Não inventar claims fora do body_text

## Claims oficiais (body_text)

- Batom hidratante altamente pigmentado
- Óleos emolientes, ceras estruturais e ativos hidratantes
- Aplicação uniforme, sensação leve, sem ressecar ao longo do dia
- Não marca linhas; aparência de lábios mais preenchidos
- Alta pigmentação imediata; conforto prolongado; hidratação contínua
- Experiência premium: embalagem sofisticada e design elegante
- Resultado: cor intensa, acabamento hidratante e uniforme

## Notas para pipeline V1

- Packshot âncora: `assets/products/classic-lips-wine/01.webp`
- Texture âncora: `02.png` se existir (swatch + bullet)
- preferred_tracks: T1 + T2; style_override default dark-feed para vídeo social
- Validar shade Wine no still gerado antes do i2v
