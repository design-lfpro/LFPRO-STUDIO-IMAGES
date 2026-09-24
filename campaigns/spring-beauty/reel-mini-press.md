---
run: spring-mini-press
campaign: Spring Beauty (22–27/09) — mini size Soft Finish de brinde
handle: po-soft-finish-claro (full-size) + mini Soft Finish Claro
track: T1-product-hero (variação "factory press")
duration_s: 13
aspect: "9:16"
text: none            # sem texto, sem end card tipográfico
status: stills-pending
---

# Spring Mini Press — briefing

## Conceito

Referência de movimento: reel Océane (prensa cromada com mola desce sobre a esteira;
o estojo entra grande e sai mini, em loop contínuo). Mantemos **só o movimento**.
Tudo que é interface de Instagram, texto e marca da referência é descartado.

**LF PRO:** o pote **Soft Finish full-size** entra na esteira, a prensa desce e, ao subir,
revela o **mini size Soft Finish**. A troca de tamanho acontece **escondida sob a prensa**:
é o corte entre o clipe 1 e o clipe 2, sem morph visível.

## Referências (assets/campaigns/spring-beauty/)

| Arquivo | Uso |
|---|---|
| `PRODUTO-CLARO.png` / `PRODUTO-MEDIO.png` | **Lock do mini**: pote preto gloss de 2 peças, tampa e base com altura parecida, monograma LF + "LF PRO" dourado no topo |
| `assets/products/po-soft-finish-claro/01.png` | **Lock do full-size**: largo e baixo, tampa em disco, sifter dourado (fechado = não aparece) |
| `27-STORY-SPRING-BEAUTY-3.png` | Proporção mini vs full-size + textura de pó em faixas |
| `27-STORY-SPRING-BEAUTY-1.png`, `27---Spring-Beauty-*.png`, `Banner-*` | **Luz da campanha**: sol natural de janela, sombras duras diagonais de persiana, taupe quente |

## Direção de arte (Spring Beauty × LF PRO)

| Elemento | Spec |
|---|---|
| Fundo | Parede taupe/areia quente #B09A85–#CDB8A0, lisa |
| Luz | **Sol natural de fim de tarde** entrando por janela; **faixas de sombra de persiana** diagonais cruzando parede, máquina e esteira; fill suave e quente |
| Esteira | Superfície matte **nude/areia** (#D8C3AA) com lâminas finas, laterais em **ouro escovado** |
| Prensa | Coluna e cabeçote em **preto laca gloss** + mola, colar e alavanca em **ouro escovado** |
| Engrenagens (1º plano, desfocadas) | Preto e ouro, bokeh quente |
| Produto | Sempre **fechado**, tampa para cima, monograma LF legível; nunca redesenhar |
| Proibido | Texto, logo gerado solto, rosa, cromado frio, mãos, rosto, pó explodindo |

## Plano (3 clipes · Kling 3.0 · 720p · first+last)

Stills em Nano Banana Pro (`imagen-nano-banana-2`, 2k, 9:16) com refs acima.

| Clipe | t | Start → End | Movimento |
|---|---|---|---|
| C1 geral | 0–5s | **S1** full-size sob prensa aberta → **S2** prensa embaixo cobrindo o pote | Esteira avança, pote para, prensa desce e comprime a mola |
| C2 close | 5–10s | **S3** close prensa embaixo → **S4** close prensa sobe, **mini** revelado | Prensa sobe devagar, mola descomprime, luz pega o dourado do mini |
| C3 geral | 10–13s | **S5** geral mini sob prensa aberta, minis à direita → **S1** | Esteira leva o mini, o próximo full-size entra = **loop** para C1 |

Montagem FFmpeg: C1 → C2 (corte seco com a prensa embaixo) → C3, sem texto; sound design mecânico leve (opcional).

## Prompts stills (EN)

Base comum (prefixar em todos):

```
Luxury cosmetics factory commercial photo, 9:16, photoreal. Warm natural late-afternoon sunlight through a window, crisp diagonal venetian-blind shadow stripes across a warm taupe wall (#B09A85), the machine and the conveyor. A nude sand matte conveyor belt (#D8C3AA) with thin slats and brushed gold side rails runs diagonally toward camera. A glossy black lacquer stamping press with a brushed gold coil spring, gold collar and gold lever arm stands over the belt. Out-of-focus black-and-gold gears in the lower foreground. Soft warm fill, gentle contact shadows, high-end beauty campaign, no text, no hands, no people.
```

- **S1:** `... Under the raised press sits the exact FULL-SIZE LF PRO Soft Finish jar from reference (wide low cylinder, closed, high-gloss piano-black, gold interlocking LF monogram and "LF PRO" on the lid, 1:1 with reference). Two more identical full-size jars wait on the belt behind it. 3/4 elevated wide shot.`
- **S2:** `same scene as S1, the press head is fully down, pressing on the jar, spring compressed; the jar is completely hidden under the gold-rimmed press head.`
- **S3:** `close-up 3/4 of the press head fully down on the belt, spring compressed, sunlight stripes on the black lacquer and gold, shallow depth of field.`
- **S4:** `same close-up, press head raised, revealing the exact MINI SIZE LF PRO Soft Finish jar from reference (small two-piece high-gloss black jar, lid and base of similar height, gold LF monogram and "LF PRO" on top, 1:1), standing where the big jar was.`
- **S5:** `same wide shot as S1, press raised, the mini jar just stamped under the press and a row of identical mini jars moving away to the right; a new full-size jar approaching from the left.`

## Prompt vídeo (Kling 3.0, por clipe)

```
Photoreal factory product commercial in warm natural window light. Smooth, precise, satisfying mechanical motion: [C1: the conveyor advances and stops, the black-and-gold press lowers and compresses the gold spring onto the jar] [C2: the press rises slowly, the spring extends, revealing the small jar] [C3: the conveyor carries the mini jar to the right while the next big jar slides in from the left]. Sunlight blind shadows stay fixed on the wall. Keep LF PRO jars and gold monogram locked to the keyframes. No morphing in view, no melting logo, no text, no hands, no camera shake.
```

## QC

- [ ] Mini e full-size fiéis às refs (proporção, 2 peças no mini, monograma)
- [ ] Troca de tamanho **só** sob a prensa
- [ ] Luz natural com sombras de persiana consistentes entre S1–S5
- [ ] C3 termina ≈ S1 (loop limpo)
- [ ] Zero texto
