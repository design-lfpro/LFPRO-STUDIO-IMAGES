---
track: T1-product-hero
status: v1-active
duration_default_s: 8
aspect: "9:16"
creative: commercial-product-turntable
---

# T1 — Product Hero (comercial de estúdio)

## Job

Vídeo de **produto real em estúdio comercial** — não packshot flutuante com “pózinho”.  
Referência mental: e-commerce premium / beauty commercial / turntable tabletop.

**Não é:** still flutuando no vazio com micro-tremor e poeira.  
**É:** produto **sobre superfície**, luz de estúdio dark, **giro / orbit** legível, desejo de compra.

## Inputs

| Input | Source |
|-------|--------|
| `handle` | run |
| Packshot | `assets/products/{handle}/01.*` (identity lock do packaging) |
| Ficha | `products/**` |
| Brand DNA | `brand-dna/` |

## Direção de arte (OBRIGATÓRIA)

| Elemento | Spec |
|----------|------|
| **Superfície** | Mesa / pedestal / stone / matte black acrylic — produto **assentado**, com contato e sombra |
| **Ambiente** | Estúdio dark: fundo charcoal/black, não flat cinza morto |
| **Luz** | Key suave + **rim** gold/cool + fill baixo (mood premium, “luz mais negra”) |
| **Câmera** | Tabletop commercial; 9:16 |
| **Motion hero** | **Slow turntable / 360 (ou 120–180°)** do produto no eixo vertical |
| **Packaging** | Travado ao packshot (logo, forma, cor) — first+last frames |
| **Proibido** | floating product no void, só “powder dust”, crash zoom no logo, face, hands UGC |

## Shot list default (1 clipe 5–8s — modo demo)

| Frame | Conteúdo |
|-------|----------|
| **START** | Produto na mesa, ângulo 3/4 frontal, logo legível, luz dark studio |
| **END** | **Mesmo setup de mesa/luz**, produto **girado** ~120–180° (outro lado do packaging ainda legível) |
| **i2v** | Interpola A→B como **giro contínuo de turntable** (não morph, não pó sozinho) |

### Shot list longo (12s / 3 cenas) — produção

| # | t | Cena |
|---|---|------|
| 1 | 0–4s | **Turntable hero** — giro na mesa |
| 2 | 4–8s | **Detail** — hold em sifter/tampa/textura (end frame safe, sem extreme logo) |
| 3 | 8–12s | **Resolve** — volta a hero 3/4 + end card FFmpeg |

## Motores

| Etapa | Modelo |
|-------|--------|
| Stills start/end | Nano Banana Pro `imagen-nano-banana-2` @ 2k + ref packshot |
| i2v default (flexível) | **Kling 3.0** `kling-30` **ou** **Seedance 2.0** `bytedance-seedance-pro-2.0` — 720p first+last, escolher por custo/fila no `simulate` |
| Premium | Veo 3.1, só se briefing pedir |
| Gate | Rita Still Verifier **antes** do vídeo |

## Prompt skeleton — STILL START (EN)

```
Luxury cosmetics product commercial still photography, 9:16.
Exact LF PRO packaging from reference photo (logo and shape locked 1:1).
Product resting on a matte black studio table / acrylic surface with realistic contact shadow,
dark beauty studio, deep black background, dramatic low-key lighting,
soft key from camera-left, subtle gold rim light, shallow depth of field tabletop,
hero 3/4 angle, packaging fully visible, logo sharp and readable,
photoreal, high-end beauty campaign, no floating product, no hands, no face, no text overlay
```

## Prompt skeleton — STILL END (EN)

```
Same scene as start: same black table, same dark studio lighting, same product identity from reference.
Product has rotated on a turntable ~150 degrees (show the other three-quarter view),
still fully on the table surface with contact shadow, logo still sharp if visible,
photoreal commercial product photography, 9:16, no floating, no extreme logo-only close-up
```

## Prompt skeleton — VIDEO / Kling 3.0 ou Seedance 2.0 (EN)

```
Photoreal product commercial. Animate ONLY as a smooth slow turntable rotation
from the start frame to the end frame on the black table.
Keep packaging and LF PRO gold monogram locked to the keyframes.
Continuous 360-style spin feel (match the rotation between frames),
cinematic tabletop lighting, subtle specular on the black lid,
no morphing, no melting logo, no crash zoom, no floating off the table,
no hands, no face, no powder explosion unless product is powder and very subtle
```

## QC gate

- [ ] Parece **produto em mesa de estúdio** (não PNG flutuando)  
- [ ] Há **giro/orbit legível** (não só poeira)  
- [ ] Logo não derrete  
- [ ] Luz dark premium  
- [ ] First+last aprovados pela Rita  

## Anti-patterns T1

- “micro push-in only” + powder dust como único motion  
- Produto flutuando no void sem superfície  
- Extreme close no monograma  
- Before/after, face, UGC banheiro  
- Seedance 1.5 Draft  
