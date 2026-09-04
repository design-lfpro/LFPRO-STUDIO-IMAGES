---
tags: [lfpro, brand-dna, studio]
status: v1
updated: 2026-08-06
sources:
  - site lfpro.com.br (91 SKUs, 552 imagens)
  - IG @lfpro.oficial (análise vault + samples estúdio)
  - copy guidelines tráfego LFPro
---

# Brand DNA — LF PRO (operacional para vídeo/imagem)

Este documento é a **lei global**. Fichas de produto especializam packaging e fórmula. Tracks especializam shot list.

> Superfície (preto+dourado) sem isto = “luxury makeup genérico”.  
> Com isto = identidade gerável.

---

## 1. Posicionamento

| Campo | Valor |
|-------|-------|
| Marca | LF PRO (Professional Makeup) |
| Território | Maquiagem & skincare de **alta performance** |
| Hero cultural | “O pó mais viralizado na internet” (Soft Eye) — usar só quando o SKU for Soft Eye |
| Tom de voz | Técnico-profissional aspiracional; sofisticado sem frieza; gaúcho leve em VO humana (“tu”) se houver VO de fundadora — em product V1 preferir **sem VO** ou VO neutra técnica |
| Público | Mulheres 23–65 (ads), núcleo 25–45; pro + consumidora final |
| Não é | Drugstore barata, glam TikTok teen, UGC banheiro, humor escatológico |

### Palavras-âncora (copy)

Performance · Profissional · Acabamento · Textura · Fórmula · Cobertura · Durabilidade · Soft focus · Aveludado · Uniforme

### Copy ads (herdado)

- Máx **1 emoji** por copy; whitelist: ✨ 🖤 🤩 💫  
- CTA recorrente: site oficial + app LFpro  

---

## 2. Sistema visual dual

### 2.1 Ecommerce packshot (verdade do produto)

Observado em **todos** os packshots oficiais baixados:

| Atributo | Spec |
|----------|------|
| Fundo | Off-white / warm white seamless (`#F5F3EF`–`#FAFAF8`), limpo |
| Sombra | Soft contact shadow, baixa opacidade, sem hard rim |
| Ângulo | 3/4 levemente elevado; produto como herói |
| Companions frequentes | Swatch de fórmula, puff, tampa aberta, stroke de creme |
| Retoque | High-end commercial, sem props de lifestyle |
| Uso no pipeline | **Identity lock** — referência obrigatória de packaging |

### 2.2 Feed / estúdio dark (vídeo social)

| Atributo | Spec |
|----------|------|
| Fundo | Preto absoluto a charcoal (`#0A0A0A`–`#1A1A1A`) |
| Accent | Dourado (`#C9A84C`–`#D4AF37`) + nudes de pele/produto |
| Luz | Key suave no produto + rim light sutil gold/cool; dramatic mas clean |
| Mood | Premium lab / beauty studio, não nightclub |
| Tipografia on-video | Mínima; preferir end card FFmpeg a texto gerado por IA |
| Uso no pipeline | Default de **T1/T2 vídeo 9:16** |

### 2.3 Cores de marca (hex de trabalho)

| Token | Hex aprox | Uso |
|-------|-----------|-----|
| `black-packaging` | `#0D0D0D` / `#111111` | Tubos, tampas, cabos |
| `gold-logo` | `#C9A227`–`#D4AF37` | Monograma LF, wordmark, pump, sifter ring |
| `cream-bg` | `#F7F5F2` | Fundo site |
| `nude-swatch-range` | `#E8D4C4`–`#8B5A3C` | Varia por SKU — ver ficha |
| `forbid-hot-pink` | — | Não usar pink marketing genérico |
| `forbid-pure-#000-crush` | — | Evitar esmagar packaging em black crush |

---

## 3. Logo lock (crítico)

Observado nos assets:

1. **Monograma LF** — duas letras entrelaçadas/geométricas em **dourado**, centro da tampa ou topo do tubo.  
2. **Wordmark “LF PRO”** — caixa alta, dourado, frequentemente sob monograma ou vertical no cabo (`LF` monogram + `/ LF PRO`).  
3. Em pincéis: gravação gold no cabo preto + código (`F01`, `C02`, `B03`).  
4. Em puffs: fita preta com monograma + `LF PRO` em gold.

**Proibido em geração:**

- Relogo inventado, “LFPro” colado, logo branco em fundo branco  
- Substituir monograma por texto genérico “PRO”  
- Logo desproporcional ou flutuando errado na tampa  

**Regra de pipeline:** se o modelo deformar logo → **re-roll** ou compor packshot real via overlay (preferível).

---

## 4. Packaging language (famílias core)

| Família | Forma | Sinais visuais |
|---------|-------|----------------|
| Soft Eye | Pote circular + tampa preta + sifter dourado perfurado + puff preta | Pó solto, swatch pulverulento |
| Soft Finish | (ver ficha) pó finalizador linha preta/gold | FPS claims no site |
| Soft Matte | Tubo preto soft-touch + **pump dourada** + texto gold “SOFT MATTE / BASE LÍQUIDA” | Swatch stroke atrás |
| Blend Cream | Pote baixo transparente/translúcido + tampa preta gold monogram | Creme batido no pote + swatch |
| Pincéis | Cabo preto brilhante, cerdas duo-tone, gold engraving | Forma anatômica por código |
| Esponjas | Preta (nova identidade), expansão molhada em claims | Object hero fácil |
| Máscara UP! | Tubo mascara preto (ver ficha) | Aplicador multifuncional |
| Classic Lips | Batom stick (ver ficha) | Cor do bullet = herói |
| Cream Color | Duo compact preto/gold | Dois wells de creme |

Detalhe por SKU: `products/**`.

---

## 5. Gramática de motion (V1)

Regra genérica de marca — **o track sempre pode especializar/sobrepor isto** (ex.: T1 exige turntable, não é só push-in). Ver `tracks/T*/README.md` antes de escrever o prompt.

| Permitido | Proibido |
|-----------|----------|
| Slow turntable / orbit 120–360° legível (hero T1) | Camera shake handheld UGC |
| Micro push-in 3–8% (detail shots / T2 macro) | Explosões de glitter |
| Slow parallax de profundidade | Morphing de packaging |
| Partículas sutis de pó (Soft Eye/Finish) | Mãos deformadas com 6 dedos (T3 exige QC) |
| Swatch “living” gloss leve | Zoom crash, whip pan, crash zoom no logo |
| Tampa / pump já no still (não animar logo) | Motion cuja **única** ação seja powder dust ou micro push (T1 exige giro legível) |
| Hold final 0.8–1.5s no hero frame | Produto flutuando sem superfície/contato |

**Empty-frame / first-last:** usar quando o modelo Magnific suportar keyframes (Kling 3.0 / Seedance 2.0 no V1); senão, still estável + motion mínimo no prompt (`locked product, fixed logo, no deformation`).

---

## 6. Áudio (V1)

| Default V1 | Spec |
|------------|------|
| VO | Off (product ASMR leve opcional: pó, pump) |
| Música | Bed suave premium ou silêncio + SFX |
| Loudness master | −14 LUFS (FFmpeg loudnorm) |
| Trendy audio IG | Fora do pipeline automatizado (manual) |

---

## 7. O que NÃO é DNA de product V1

- Storytelling P&B da fundadora  
- Collab influencer / UGC  
- Carrossel de specs com tipografia densa (outro pipeline: HTML→PNG)  
- Before/after de cobertura (T5)  
- Shade finder multi-rosto (T5+)  

---

## 8. Casting (só a partir da V2)

Quando o cliente enviar banco de modelos:

- Guardar em `assets/cast/{model_id}/`  
- Character lock: mesmas fotos âncora, alterar rosto **leve** só se pedido  
- V2 T4: holding product / clean beauty — **não** reescrever maquiagem do produto na pele sem protocolo  

Ver `brand-dna/casting-v2.md`.

---

## 9. Anti-patterns globais (lista de banimento de prompt)

```
bathroom selfie lighting, harsh phone flash, cluttered vanity mess,
comic sans, heavy pink filters, drugstore plastic look, wrong logo,
deformed LF monogram, melting packaging, extra fingers, waxy mannequin skin,
teen e-girl makeup, male presenter (unless explicit),
before-after split face (unless track T5),
readable fake ingredients text, random watermarks
```

---

## 10. Hierarquia de fontes da verdade

1. Packshot local `assets/products/{handle}/01.*`  
2. Ficha SKU + `_family.md`  
3. Este Brand DNA  
4. Claims `assets/catalog/claims-slim.json` / body site  
5. Referências IG em `_research/` e `assets/refs/`  

Conflito: **packshot e ficha vencem** o prompt criativo.
