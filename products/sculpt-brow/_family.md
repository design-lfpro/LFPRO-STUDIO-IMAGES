---
family: sculpt-brow
title: Sculpt Brow
product_type: Lápis para Sobrancelha
status: novo-produto-pendente-cadastro
preferred_tracks: [T1-product-hero, T4-model-portrait]
blocked_tracks: [T5-face-proof]
handles:
  - sculpt-brow-light
  - sculpt-brow-medium
  - sculpt-brow-dark
---

# Sculpt Brow — DNA de família

Linha de **lápis para sobrancelha** LF PRO. **Produto novo — sem ficha/catálogo prévio neste repo.** Catalogado a partir de fotos reais já enviadas anteriormente ao Magnific (uploads do usuário, projeto "SOCIAL MEDIA"), não a partir de Drive nesta sessão.

## ⚠️ Pendências desta cadastro (não inventar)

- **Nomes oficiais dos tons — CONFIRMADO (2026-09-08):** ​**Light, Medium, Dark**.
- **SKU e preço:** não encontrados — produto não está no catálogo Shopify (`assets/catalog/products-index.json`) nem tem página no site.
- **"JC" no packaging — RESOLVIDO (2026-09-08):** usuário confirmou que "JC" **não existe** no produto real — a legenda automática do Magnific na foto `SCULPT BROW DIVERSAS 04` leu errado o **monograma LF** (logo da marca) como se fosse texto "JC". É o logo LF de sempre, não uma collab. Removida a suposição de collab.
- **Packshot binário:** os arquivos de referência estão hospedados no Magnific (uploads do usuário), mas esta sessão não conseguiu baixar o binário para `assets/products/` (host `pikaso.cdnpk.net` bloqueado pela política de rede do sandbox — mesma limitação de outras sessões). Os links `webUrl` abaixo servem como referência até o usuário reenviar as fotos via Google Drive (mesmo fluxo usado para Essential Lips) para publicarmos o arquivo local oficial.

## Packaging (lock visual) — NUNCA redesenhar

| Elemento | Lock |
|----------|------|
| **Corpo** | Lápis fino, cilíndrico, casing preto matte |
| **Logo/texto** | Lettering gold foil `SCULPT BROW` ao longo do corpo |
| **Ponta** | Afiada, revela o pigmento colorido do tom (marrom/grafite/bege conforme o tom) |
| **Fundo referência** | Bege/branco, still de estúdio |

## Tons — Light, Medium, Dark (confirmado pelo usuário)

3 tons oficiais: **Light, Medium, Dark**. Mapeamento tom↔foto abaixo é parcial — só o que o **nome do arquivo original** confirma; "bege" no nome de outros arquivos é o **fundo do still** (background bege), não o nome do tom, então não foi usado para mapear.

| Tom | Foto com nome de arquivo confirmando | Observação |
|-----|----------------------------------------|------------|
| **Light** | `sculpt-brow-produto-light-zoom.png` (creation `CqHBShAEEy`) — close-up produto | Ponta com pigmento castanho mais claro na legenda automática |
| **Medium** | `sculpt-brow-medium-foco.png` (creation `rglYYXtxtc`) — foto de modelo, não produto isolado | Sem still de produto isolado confirmado ainda |
| **Dark** | `sculpt-brow-modelo-site-dark.png` (creation `CqFMxe9EEy`) — foto de modelo, não produto isolado | Sem still de produto isolado confirmado ainda |

- As fotos com 3 lápis juntos (`vumR99ca47`, `huEMD6fvqL`, `l71IkzBgv9`, `8vp6XY4IrU`) provavelmente mostram os 3 tons lado a lado, mas sem confirmação de qual posição é qual tom — não assumir ordem.
- Hex não extraídos ainda (sem acesso ao binário nesta sessão) — pendente.
- **Falta still de produto isolado (packshot) para Medium e Dark** — só temos fotos de modelo aplicando para esses dois tons.

## Referências reais (Magnific — uploads do usuário)

- Produto (3 lápis, still limpo): https://www.magnific.com/app/creation/vumR99ca47
- Produto (vertical, gold lettering): https://www.magnific.com/app/creation/l71IkzBgv9
- Produto (diagonal): https://www.magnific.com/app/creation/8vp6XY4IrU
- Produto com strokes/swatch (3 tons juntos, posição não confirmada): https://www.magnific.com/app/creation/huEMD6fvqL
- Produto Light (close-up confirmado pelo nome do arquivo): https://www.magnific.com/app/creation/CqHBShAEEy
- Detalhe produto (fundo bege, tom não confirmado): https://www.magnific.com/app/creation/bxKNa465Y2
- Detalhe produto (fundo bege, tom não confirmado): https://www.magnific.com/app/creation/gOJqblrSXO
- Produto still (fundo bege, "diversas"): https://www.magnific.com/app/creation/xSgF2ptjfW — legenda automática leu o monograma **LF** como "JC" por engano; é o logo normal da marca, confirmado pelo usuário
- Modelo Dark aplicando: https://www.magnific.com/app/creation/CqFMxe9EEy
- Modelo Medium, foco sobrancelha: https://www.magnific.com/app/creation/rglYYXtxtc

## Modelos (library Magnific — já cadastrados)

- `sculpt-brow-modelo-light` (id 2151468)
- `sculpt-brow-modelo-medium` (id 2151475)
- `sculpt-brow-modelo-dark` (id 2151480)

## Product library asset (Magnific)

- `@sculpt-brow-pencil` (id 2262864) — criado a partir de `vumR99ca47`

## Claims (site — sem inventar)

- **Nenhum claim oficial disponível** — produto sem página publicada, sem body_text

## Prompt anchors (EN) — família

```
LF PRO Sculpt Brow eyebrow pencil identity lock: slim cylindrical pencil, matte black casing, gold foil lettering "SCULPT BROW" along the barrel, sharpened tip revealing pigment color, off-white or beige studio background, photorealistic product photo, no redesign of shape or logo, exact tip color per shade.
```

## Anti-patterns

- Redesenhar formato do lápis, cor do corpo ou lettering
- Inventar nomes de tons, SKU ou preço
- Assumir/afirmar collab "JC" sem confirmação
- Full-face proof (T5 bloqueado)

## Notas V1

- Cadastro iniciado a partir de imagens já existentes no Magnific (não desta sessão) — sem arquivo físico ainda em `assets/products/sculpt-brow/`
- Próximo passo sugerido: usuário reenviar fotos oficiais via Drive (com nomes de tom no arquivo, como foi feito com Essential Lips) para completar o cadastro com packshot local + hex reais + nomes de tom confirmados
