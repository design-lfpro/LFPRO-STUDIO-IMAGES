---
family: essential-lips
handles: ['essential-lips-beige', 'essential-lips-rose', 'essential-lips-blush', 'essential-lips-malt', 'essential-lips-mauve', 'essential-lips-clay', 'essential-lips-carmin', 'essential-lips-wine']
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
status: dna-v1-scaffold
lancamento: "2026-09-09"
updated: 2026-08-20
---

# Família `essential-lips`

Batom líquido **matte** LF PRO. Linha nova (lançamento 09/09) — 8 tons, do nude ao vermelho intenso. Volume 4,5 mL, aplicador doefoot de precisão.

## Assets — packshot real disponível

Fotos de estúdio reais (fundo cinza neutro, cubo branco, iluminação soft) já estão em `assets/products/essential-lips-{tom}/01.jpeg`, uma por tom — vieram do Google Drive do time (pasta "ESSENTIAL LIPS 🫟" / "PARA APROVAR"). Cada foto mostra o frasco fechado + o frasco aberto com o aplicador ao lado.

**Atenção — ainda não é o packshot final de e-commerce:** o fundo é cinza de estúdio, não o off-white `#F7F5F2` do site (ver `assets/products/essential-lips-*/site/` quando o time subir a versão com fundo de e-commerce — há um PSD "SITE ESSENTIAL LIPS.psd" e uma pasta "site" no Drive ainda não exportados como imagem final). Para **shape/logo/proporção/cor do líquido** este still já vale como identity lock; para o **fundo/luz** de still V1 dark-feed ou ecommerce, seguir os specs do brand-dna (a foto de estúdio cinza não é nem um nem outro).

Rodar Ana Produto (`opensquad/agents/ana-produto.agent.md`) sobre `01.jpeg` de cada tom para lock list 1:1 antes de qualquer still de entrega.

## Correção de nome de tom

O infográfico de lançamento (comunicação) grafa o 5º tom como "**Malve**", mas o nome oficial do produto — confirmado nas fotos de estúdio, nos arquivos de textura do Drive e nas etiquetas físicas dos frascos de teste — é "**MAUVE**". Este repositório usa `essential-lips-mauve` como handle. Se o site/embalagem final usar "Malve" em algum material de marketing, sinalizar a inconsistência antes de publicar.

## Packaging (lock — confirmado por foto de estúdio + arte de fábrica)

Fonte: fotos reais `assets/products/essential-lips-{tom}/01.jpeg` + desenho de arte do fornecedor (`Batom Essential Lips LFpro.pdf`, código de produto **SN322 21**, Drive).

1. **Frasco**: corpo em vidro/acrílico **fosco (frosted) translúcido**, formato colunar levemente retangular de ombros retos — o líquido colorido é visível por trás do fosco, dando um efeito "leitoso" sobre a cor real.
2. **Tampa**: preta, cilíndrica, com rosca/ranhura horizontal visível na parte superior (textura de grip); rosqueia sobre o gargalo do frasco.
3. **Impressão no corpo do frasco** (não na tampa): monograma **LF** dourado estilizado (duas letras entrelaçadas, ligeiramente itálico) centralizado, com wordmark **"LF PRO"** dourado em caixa alta logo abaixo, menor. Zona de impressão ~65,94 mm largura × 55 mm altura (spec de arte do fornecedor).
4. Duas linhas horizontais finas (stripe dourado/preto) demarcam uma faixa de ~14 mm entre o ombro do frasco (base da tampa) e a área do monograma — visível nas fotos como um "colarinho" logo abaixo da rosca.
5. **Aplicador (doefoot)**: haste preta fina + ponta oval afunilada em veludo/esponja fiapada (formato "doefoot" clássico), destacável, mostrada separada do frasco nas fotos de still — fica dentro da tampa quando fechado. **Confirmado por foto real do produto físico (03/09):** a textura fiapada/afelpada do veludo aparece **mesmo com produto aplicado em cima** — não é uma cúpula lisa e uniformemente brilhante (a referência tipo Summer Fridays usada em alguns prompts é mais lisa que o real); a aplicação real sai um pouco irregular/manchada na transição haste-produto. Descrever assim em prompts de still de aplicador: "the velvet fiber texture of the doe-foot tip remains visible through the product coating, not a smooth glossy dome — slightly uneven/streaked product coverage near the base, like a real-world application, not a perfect studio dip."
6. Sem texto do nome do tom impresso no frasco (a identificação de tom é só por cor do líquido + rótulo/caixa secundária).

**Não confirmado ainda:** acabamento exato do vidro (fosco por jateamento vs. fosco de fábrica), se há brilho/verniz na tampa (parece semi-glossy nas fotos) — validar com Ana Produto still a still.

### Regra — produto aberto sempre com aplicador (SEM EXCEÇÃO, inclusive na mão de modelo)

Em **qualquer** still/vídeo — produto sozinho, still de still-life, still com mão, still com modelo segurando o produto, still de campanha, still de combo — o frasco só pode aparecer de dois jeitos:

1. **Fechado**, com a tampa colocada; ou
2. **Aberto**, com o **aplicador doefoot visível junto** (na mão, encostado, ou saindo da tampa ao lado).

**Nunca** gerar (ou aceitar) um frasco aberto sem o aplicador aparecer — mesmo que o still seja de uma modelo segurando o produto e o foco seja o rosto dela. Essa regra é um **checklist obrigatório de todo prompt de still de produto/modelo+produto** desta linha, não só de still-life. Declarar explicitamente no prompt qual dos dois estados (fechado OU aberto+aplicador) antes de gerar — nunca deixar implícito.

### Regra — escala real do frasco

Frasco é **pequeno e fino**: altura total (com tampa) ~9–10 cm, diâmetro da tampa ~1,7 cm (mais estreita que um polegar). Em qualquer still com mão/modelo segurando o produto, o frasco deve caber entre 2–3 dedos com sobreposição visível — nunca desenhar maior que isso. Referência real: `assets/products/essential-lips-wine/tamanho-real-1.jpeg` e `tamanho-real-2.jpeg` (fotos do frasco fechado numa mão real).

**Regra — proporção travada (erro confirmado: frasco sai ora esticado, ora curto demais).** Não basta dar altura/diâmetro em cm soltos — declarar a **proporção** explicitamente, porque a IA erra escala mesmo tendo os números:

> "the bottle's height-to-width ratio is fixed at approximately 5.5:1 — a slim, elongated column, not stubby or squat, and not stretched thinner/taller than that ratio. The cap is roughly one-third of the total bottle height. Match these proportions exactly to the reference photo — do not lengthen, shorten, widen, or narrow the silhouette."

Incluir essa frase (ou equivalente) junto da descrição de escala em todo prompt com o frasco visível — a régua em cm sozinha não é suficiente.

### Regra — fundo padrão da campanha

**Fundo preto sólido (`#0A0A0A`) é o padrão de toda a campanha Essential Lips** (hero de produto, still com modelo, swatch/textura, stories) — só usar outro fundo/cor se for explicitamente pedido para aquela peça específica.

### Regra — fidelidade do logo (descrever a geometria, não só "logo dourado")

Logo distorcido é o erro mais recorrente e mais caro (retrabalho + créditos). "Gold LF monogram" sozinho no prompt não é suficiente — a IA precisa da geometria descrita, e a versão abaixo já foi endurecida depois de ver erros reais (texto espelhado/invertido, símbolo virando losango/quadrado genérico):

> "the LF monogram is a two-letter geometric logotype — 'L' and 'F' interlocked in a tall, narrow, architectural/deco construction, flat gold foil color (not chrome, not 3D, not a gradient), crisp straight edges. It is NOT a diamond, NOT a shield, NOT a wreath, NOT a swirl, NOT a generic abstract mark — it is specifically the two letterforms L and F and nothing else. Directly below it, in smaller gold capital letters, the wordmark 'LF PRO' — reading correctly left-to-right, never mirrored, never backwards, never reversed. Reproduce this exact logotype faithfully from the reference photo — same proportions, same letterforms, same relative size to the bottle — do not substitute, simplify, or reinterpret it into a different symbol."

Incluir esse parágrafo (ou equivalente) em **todo** prompt que tenha o frasco visível de forma legível — não só copiar "gold LF monogram" solto.

**Regra — a tampa é PRETA, o dourado é só no logo.** Erro recorrente confirmado visualmente (03/09): a tampa sai dourada/rose-gold inteira, ou até branca/creme, em vez de preta — provavelmente porque "gold rim light" + "gold LF monogram" no mesmo prompt faz a IA "vazar" o dourado pra tampa toda. Incluir sempre, de forma explícita e separada: *"the cap is solid glossy BLACK plastic/lacquer — NEVER gold, NEVER rose-gold, NEVER white or cream. Gold appears ONLY on the printed monogram and wordmark on the bottle body, nowhere else on the packaging."*

**Risco real não é "macro" — é complexidade de cena.** Levantamento de 28/08-03/09: stills de produto puro (2-3 frascos, sem modelo, framing próximo do packshot original) saíram fiéis quase sempre. O que falhou consistentemente:
- **4+ frascos na mesma geração** (cascata de 8, flat lay de 4) — cada frasco extra dilui a "atenção" do modelo pros detalhes do logo de cada um.
- **Modelo (rosto/mão fotorreal) + produto no mesmo frame** — a IA prioriza anatomia/pele coerente sobre fidelidade de um elemento pequeno e secundário (o logo), mesmo em enquadramento não-macro.

Nano Banana **não copia pixel do packshot real** — ele reinterpreta a cena inteira a cada geração; quanto mais elementos concorrendo (mais frascos, ou frasco+rosto+mão), maior o erro acumulado no logo. Reforçar a descrição da geometria (acima) ajuda mas **não elimina** o risco nesses cenários.

Diante disso:
- **Produto puro, hero de packaging**: manter simples — 1-3 frascos por still, sem modelo. É a composição com maior taxa de acerto; preferir sempre que o pedido permitir.
- **Still com modelo + produto**: aceitar de partida que a taxa de acerto de primeira é baixa — orçar mentalmente 2-3 gerações, não 1. Perguntar ao time antes de rodar 3 variações diferentes de uma vez (evita gasto em lote quando uma trava o logo) — **gerar 1 de cada vez** e só seguir pra próxima depois de confirmação.
- **Still com 4+ frascos**: quando o pedido não exige literalmente todos juntos numa imagem só, sugerir dividir em 2 gerações menores (ex.: 2×4 em vez de 8×1) antes de tentar o still cheio.

**Gate de verificação — limitação atual:** o pipeline (`tracks/T1/README.md`) prevê uma etapa de still verifier (Rita/Ana Produto) antes de aprovar um still. O agente não consegue abrir a URL de imagem gerada no Magnific (`pikaso.cdnpk.net`) sozinho — bloqueio de rede da organização, não contornável de dentro da sessão. **Fix prático:** o time cola a imagem gerada direto no chat (imagem colada é visível ao agente, diferente de link) — isso fecha o gate de verificação real: o agente confere o logo/still com os próprios olhos antes de seguir pra próxima etapa, em vez de descobrir erro só depois de entregue. Vale pedir isso sempre que o still for crítico de logo. Alternativa mais lenta: salvar a imagem aprovada no Drive, de onde o agente consegue puxar normalmente.

**Regra — sempre informar custo em créditos antes de rodar.** Toda operação paga (generate, upscale, remove background, relight, etc.) tem custo diferente por modo/escala — **nunca assumir** que uma é "mais barata" sem checar (ex.: upscale `ultra-photo` 2x saiu mais caro que um generate inteiro). Antes de rodar, informar o custo em créditos ao time e, quando fizer sentido, a opção mais barata que atinge o mesmo objetivo — deixar o time decidir, não assumir.

### Regra — orientação do aplicador em still boca/rosto

Quando o aplicador (doefoot) aparece perto da boca da modelo (still de still com produto aberto encostando/aplicando), **a ponta que acumula produto (a esponja/veludo) deve estar virada para o lado da boca/ponto de contato** — nunca de costas ou apontando para longe do rosto. Declarar essa orientação explicitamente no prompt sempre que o still envolver boca + aplicador.

## Ficha técnica (fonte: infográfico de lançamento)

| Campo | Valor |
|-------|-------|
| Categoria | Maquiagem — Batom líquido |
| Acabamento | Soft matte aveludado |
| Volume | 4,5 mL |
| Lançamento | 09/09 |
| Valor | R$ 69,90 |
| Público-alvo | Adultos |
| Registro ANVISA | Cosmético — Notificação (Grau 1) |
| Fragrância | Sim (alérgenos declarados conforme RDC 17/2021) |
| Fabricante | BF Cosméticos e Produtos para a Saúde Ltda — CNPJ 30.819.966/0001-16 (fonte: dizeres de rotulagem) |

## Selos / atributos da linha

Vegano · Sem parabenos · Não testado em animais · Alta cobertura · Com manteigas hidratantes

## Composição (INCI completo — fonte: "Dizeres de Rotulagem Batom Líquido LF PRO")

Isododecano · Decametilciclopentasiloxano · Sílica · Polibuteno · Hectorita Diesteardimônio · Butil-Hidroxitolueno (BHT) · Ozoquerita · Octinoxato (Ethylhexyl Methoxycinnamate) · Parafina Líquida · Copolímero de Estireno Hidrogenado/Isopreno · Fenoxietanol · Trimetilsiloxissilicato · Triglicerídeo Caprílico/Cáprico · Manteiga de Karité (Butyrospermum Parkii) · Manteiga da Semente de Cacau (Theobroma Cacao) · Octenilsuccinato de Amido Alumínio · Perfume · Cinamaldeído · Citral · Eugenol · Limoneno. Pode conter os corantes: CI 77891 (branco), CI 12085, CI 77499 (preto), CI 77492 (amarelo), CI 77491, CI 45410, CI 15850, CI 77007 (azul), CI 15880.

Tradução de uso comercial dos ingredientes-chave (para copy) na seção de tecnologia abaixo — **usar sempre o nome comercial/tradução, nunca colar a lista INCI em peça de consumidor.**

## Tecnologia / composição (para explicar em conteúdo de bastidores)

- **Sistema volátil** (isododecano + decametilciclopentasiloxano como veículo): evapora após a aplicação, deixando apenas pigmento e formadores de filme aderidos aos lábios.
- **Formadores de filme** (copolímero de estireno hidrogenado/isopreno, trimetilsiloxissilicato): dão aderência, resistência à água/transferência e acompanham o filme depois da secagem.
- **Hectorita diesteardimônio**: agente de suspensão/textura, ajuda a estabilizar o pigmento na fórmula.
- **Sílica**: efeito soft focus, contribui pro acabamento matte/aveludado (evita aspecto craquelado).
- **Manteiga de Karité**: hidratação profunda, cuidado da barreira dos lábios.
- **Manteiga de Cacau**: emoliente, nutritiva, conforto.
- **Antioxidante (BHT)**: protege a fórmula e a cor.
- **Octinoxato (Ethylhexyl Methoxycinnamate)**: consta na fórmula como filtro UVB — **ver regra crítica de FPS abaixo, nunca comunicar como fotoproteção**.

## Modo de uso (parte essencial da venda — sempre citar em conteúdo educativo)

1. Lábios limpos e secos.
2. Retirar o excesso do aplicador na borda do frasco.
3. Aplicar começando pelo centro, levando o produto em direção aos cantos.
4. Aguardar **~60 segundos** para a secagem completa.
5. Para mais intensidade, construir uma segunda camada respeitando o tempo de secagem.
6. Gloss por cima é permitido, mas só **depois** da secagem completa.

Ponto de educação mais importante: **menos produto + aplicação uniforme + tempo de secagem.**

---

## Claims e guardrails de comunicação (fonte: "Direcionamento Time Essential Lips v2")

Esta seção é **regra dura** para qualquer agente de copy (Vini, Theo, Bia, Duda, Rita) neste projeto — prevalece sobre qualquer instinto genérico de "vender mais forte". Nenhum conteúdo desta linha sai sem passar por este checklist.

### Conceito central

**"Matte, mas confortável."** Não vender como "o que não sai nunca". Vender a experiência: cor intensa, acabamento aveludado, aplicação fluida, filme flexível. Matte confortável não é matte seco.

Palavras-chave: matte confortável · aveludado · alta cobertura · cor intensa · filme flexível · conforto · longa duração (como proposta, não número) · 8 tons essenciais · cartela objetiva e essencial.

Tom: sofisticado, seguro, técnico na medida certa, próximo.

### ✅ O que PODEMOS comunicar

| Pilar | Mensagem aprovada | Como provar/mostrar |
|-------|--------------------|-----------------------|
| Acabamento | Soft matte / matte confortável / acabamento aveludado | Close nos lábios e swatches após a secagem |
| Cobertura | Alta cobertura, buildável (1 camada x 2 camadas) | Mostrar cobertura real, camada única vs. construída |
| Conforto | Textura confortável, filme flexível, toque non-sticky | Aplicação, movimento dos lábios, relato sensorial |
| Fórmula | Sistema volátil + formadores de filme + Karité e Cacau | Conteúdo de bastidores, explicação de ingredientes |
| Resistência | Tecnologia de formação de filme, resistência à água/transferência **como característica técnica**, não garantia | Falar da tecnologia sem virar promessa absoluta |
| Aplicação | Doefoot de precisão; pouca quantidade já pigmenta bem | Demonstração do aplicador, aplicação controlada |
| Cartela | 8 tons, do nude ao vermelho intenso | Swatches em diferentes fototipos e subtons, sem filtro que altere a cor |

### 🚫 O que NÃO podemos prometer — NUNCA usar como promessa absoluta

- "Dura 8, 10 ou 12 horas" como garantia (não há teste que sustente número de horas)
- "Não transfere" como afirmação universal / "100% à prova de transferência"
- **"FPS X" ou "protege do sol" como benefício de fotoproteção comprovado — não há teste de FPS.** O octinoxato consta na composição como filtro UVB, mas isso NÃO autoriza comunicar fator de proteção.
- "Indestrutível", "não sai nunca", "à prova de tudo" ou equivalentes
- "Não marca nenhuma linha" como promessa absoluta para todo mundo (pode falar em "visual uniforme", não em garantia universal)
- "Película rígida" — a fórmula é filme **flexível**, nunca falar em película rígida

### Como falar de longa duração (sem quantificar)

Explicar o **porquê** a fórmula tende a durar, não prometer número: sistema volátil evapora e deixa filme colorido → formadores de filme dão aderência e resistência → filme é flexível, acompanha o movimento → sílica e formadores contribuem pro acabamento soft matte e controle de oleosidade. Resultado desejado = boa permanência sem abrir mão do conforto.

### Como falar de transferência

Frase segura: *"A fórmula foi desenvolvida com tecnologia de formação de filme que favorece a resistência à transferência após a secagem completa."* Sempre mencionar a importância da secagem completa (~60s). Evitar teste improvisado em vídeo como "prova" de não transferir — se aparecer demonstração, apresentar como aquele uso específico, nunca como garantia universal.

### FPS / filtro UVB — atenção máxima

A fórmula contém Octinoxato (filtro UVB na composição), mas **não há teste de FPS**. Proibido: número de FPS, "fator de proteção", posicionar o batom como fotoprotetor. Resposta pronta se perguntarem: *"A fórmula contém um ingrediente com função de filtro UVB, mas não temos teste de FPS. Por isso, não comunicamos um fator de proteção."*

### Ingredientes — tradução para o consumidor

| Ingrediente | Tradução |
|-------------|----------|
| Manteiga de Karité | Ajuda a manter os lábios confortáveis e cuidados |
| Manteiga de Cacau | Contribui para nutrição e conforto |
| Sílica | Ajuda a construir o efeito matte/aveludado |
| Sistema de formação de filme | Ajuda a criar a película que adere aos lábios após a secagem |
| Copolímero elastomérico | Ajuda o filme a acompanhar o movimento dos lábios, contribui pro conforto |

### Frases prontas para o time

- "É matte, mas não tem aquela sensação de lábio duro e seco."
- "O acabamento é soft matte: aveludado, confortável e com cor intensa."
- "A fórmula foi pensada para formar um filme flexível depois da secagem."
- "Tem alta cobertura, mas você consegue construir a intensidade em camadas."
- "O diferencial está em unir tecnologia de longa duração com ingredientes de conforto, como Karité e Cacau."
- "Aguarda cerca de 60 segundos para secar completamente — esse passo faz diferença no resultado."
- "São 8 tons, do nude ao vermelho intenso, pensados para diferentes estilos e peles."
- "É aquele matte bonito: aveludado, confortável e com cor intensa."
- "A fórmula forma um filme flexível que acompanha o movimento dos lábios."
- "É uma cartela essencial: 8 cores escolhidas para você encontrar do nude ao vermelho intenso."
- "Você pode usar uma camada para um efeito mais leve ou construir a cor para um resultado mais marcante."

### Perguntas difíceis — como responder

- **"Dura quantas horas?"** → "A proposta é de longa duração, mas não queremos prometer um número fixo porque isso varia conforme alimentação, atrito, oleosidade, quantidade aplicada e rotina. A fórmula usa tecnologia de formação de filme e precisa secar completamente."
- **"Não transfere?"** → "A fórmula foi desenvolvida para favorecer a resistência à transferência após a secagem, mas não prometemos 100% de transferência zero em qualquer situação."
- **"Tem FPS?"** → "A fórmula contém um ingrediente com função de filtro UVB, mas não temos teste de FPS. Por isso, não comunicamos um fator de proteção."
- **"Resseca os lábios?"** → "A proposta é unir matte e conforto, com manteigas de Karité e Cacau. A percepção pode variar de pessoa para pessoa; recomendamos lábios limpos e bem cuidados antes da aplicação."
- **"Posso passar gloss por cima?"** → "Sim, depois da secagem completa."

### Direção criativa sensorial (para still/vídeo, além de performance)

- Close de aplicação: mostrar a fluidez do produto deslizando nos lábios.
- Antes/depois da secagem: evidenciar transformação de textura cremosa → acabamento soft matte.
- Movimento: falar, sorrir, movimentar os lábios pós-secagem para comunicar "filme flexível" (ótimo argumento de vídeo).
- Swatches: os 8 tons em sequência, cor real, sem filtro que altere a cor.
- Camadas: 1 camada (leve) vs. construção (intensa).
- Textura real dos lábios preservada — evitar excesso de blur/filtro que apague a pele.
- Diversidade de fototipos e subtons nos swatches.

Sensação-alvo: *"Você olha e vê um matte bonito. Você aplica e percebe o conforto."*

### Checklist pré-publicação (rodar sempre antes de aprovar copy desta linha)

- [ ] Falei de acabamento, cobertura, conforto ou tecnologia — sem prometer resultado não testado?
- [ ] Evitei número de horas de duração?
- [ ] Evitei afirmar "100% não transfere"?
- [ ] Não mencionei FPS ou fator de proteção?
- [ ] Expliquei o tempo de secagem quando há demonstração?
- [ ] Mostrei a cor real em pele/lábios quando possível, sem filtro que altere a cor?
- [ ] Linguagem de experiência e formulação, sem transformar ingrediente em promessa clínica?

## Anti-patterns

- Qualquer claim da lista "NÃO podemos prometer" acima
- Número de FPS em qualquer peça
- Película rígida / batom "indestrutível"
- T5 (full-face proof) — bloqueado neste V1
- Logo LF PRO alterado ou genérico; monograma fora da zona de impressão (~65,94×55mm no corpo do frasco, nunca na tampa)
- Usar "Malve" em vez de "Mauve" sem sinalizar a inconsistência (ver seção acima)
- Fundo cinza de estúdio das fotos-fonte como fundo final de still de entrega (usar dark-feed ou ecommerce off-white conforme brand-dna)
- Frasco aberto sem o aplicador aparecer junto (ver regra acima — ou aplicador junto, ou frasco fechado com tampa)
- Frasco desproporcionalmente grande em still com mão/modelo (ver regra de escala real acima)
- Fundo diferente de preto sólido sem pedido explícito pra aquela peça
