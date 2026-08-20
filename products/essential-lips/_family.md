---
family: essential-lips
handles: ['essential-lips-beige', 'essential-lips-rose', 'essential-lips-blush', 'essential-lips-malt', 'essential-lips-malve', 'essential-lips-clay', 'essential-lips-carmin', 'essential-lips-wine']
preferred_tracks: [T1-product-hero, T2-texture-macro]
blocked_tracks: [T5-face-proof]
status: pre-lancamento-sem-packshot
lancamento: "2026-09-09"
updated: 2026-08-20
---

# Família `essential-lips`

Batom líquido **matte** LF PRO. Linha nova (próximo lançamento, 09/09) — 8 tons, do nude ao vermelho intenso. Volume 4,5 mL, aplicador doefoot de precisão.

## ⚠️ Status de assets — aguardando packshot oficial

**Não existe ainda foto oficial do produto em `assets/products/essential-lips-{tom}/01.*`.** O material disponível hoje é:

1. Infográfico de lançamento (render de embalagem + swatches dos 8 tons + ficha técnica) — usado só como referência visual provisória, **não é packshot 1:1**.
2. Documento interno "Direcionamento Time Essential Lips" (guardrails de comunicação, ver seção Claims abaixo).

Enquanto o packshot real não chegar em `assets/products/essential-lips-{handle}/01.*`:

- **Não gerar stills finais de entrega** em identity lock (regra 1 do `CLAUDE.md` — nunca redesenhar packaging a partir de aproximação).
- Pipeline pode rodar até shotlist/prompt-draft (steps 01–04), mas o still lock (step 05+) fica bloqueado até asset real.
- Quando o packshot chegar: rodar Ana Produto (`opensquad/agents/ana-produto.agent.md`) para extrair lock list 1:1 e atualizar esta ficha + as 8 fichas de tom.

## Packaging (observado no infográfico — provisório)

- Frasco cilíndrico, base em vidro/acrílico fosco escurecido que deixa entrever o líquido colorido na parte inferior
- Tampa preta cilíndrica, glossy
- Monograma **LF** dourado + wordmark **LF PRO** dourado, centralizado no corpo do frasco
- Aplicador tipo **doefoot** (haste + ponta em esponja/aplicador de precisão), visível separado do frasco em uma das cenas do material
- Sem texto de nome do tom impresso no frasco

**Não confirmado até packshot real:** proporção exata cap/frasco, textura do vidro (fosco vs. transparente fumê), acabamento metálico do aro (se houver).

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

## Selos / atributos da linha

Vegano · Sem parabenos · Não testado em animais · Alta cobertura · Com manteigas hidratantes

## Tecnologia / composição (para explicar em conteúdo de bastidores)

- **Sistema volátil** (isododecano como veículo): evapora após a aplicação, deixando apenas pigmento e formadores de filme aderidos aos lábios.
- **Formadores de filme**: dão aderência, resistência à água/transferência e acompanham o filme depois da secagem.
- **Copolímero elastomérico**: confere flexibilidade ao filme final — acompanha o movimento natural dos lábios, contribui pro toque non-sticky.
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

- Inventar packaging antes do packshot oficial chegar (ver aviso no topo)
- Qualquer claim da lista "NÃO podemos prometer" acima
- Número de FPS em qualquer peça
- Película rígida / batom "indestrutível"
- T5 (full-face proof) — bloqueado neste V1
- Logo LF PRO alterado ou genérico
