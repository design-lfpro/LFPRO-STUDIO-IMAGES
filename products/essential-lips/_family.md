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
5. **Aplicador (doefoot)**: haste preta fina + ponta em veludo/esponja afunilada (formato "doefoot" clássico), destacável, mostrada separada do frasco nas fotos de still — fica dentro da tampa quando fechado.
6. Sem texto do nome do tom impresso no frasco (a identificação de tom é só por cor do líquido + rótulo/caixa secundária).

**Não confirmado ainda:** acabamento exato do vidro (fosco por jateamento vs. fosco de fábrica), se há brilho/verniz na tampa (parece semi-glossy nas fotos) — validar com Ana Produto still a still.

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
