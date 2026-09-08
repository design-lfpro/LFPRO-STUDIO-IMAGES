# Sculpt Brow — DNA da família

Lapiseira retrátil LF PRO para sobrancelhas. Lançamento recente (pasta Drive `0813 - SCULPT BROW LANÇAMENTO`) — 3 tons: Light, Medium, Dark. Ainda não integrada ao catálogo mestre (`assets/catalog/*.json`, snapshot de 19/08, anterior a este lançamento).

## Assets — packshot real disponível

`assets/products/sculpt-brow-{light,medium,dark}/01.png` — packshot oficial fundo off-white, produto fechado ao lado da tampa (fonte: pasta "FOTO PRODUTO" dentro de "SCULPT BROW" no Drive).

## Identidade do produto

Lapiseira retrátil desenvolvida para criar sobrancelhas naturalmente definidas. Ponta chanfrada com **duas funções**: extremidade fina pra desenhar fios ultrafinos, face mais ampla pra preencher falhas com rapidez. Depois do uso, basta pressionar suavemente a ponta contra uma superfície plana pra remodelar o formato chanfrado (mecanismo auto-apara, sem precisar de apontador separado).

Headline de marca: *"O destaque do seu olhar está nos detalhes"* / *"Sobrancelhas definidas com efeito natural"* / *"Simples, elegante e precisa"* / *"Precisão na medida certa"*.

## Packaging (lock visual — confirmado por foto real)

1. **Corpo**: lapiseira fina, cilíndrica, preta fosca/semi-glossy, formato de caneta/lapiseira de precisão (não é lápis de madeira tradicional).
2. **Ponta**: mecanismo retrátil — quando estendida, mostra a mina em formato **chanfrado** (bisel, tipo cinzel), cor do tom visível na ponta.
3. **Impressão no corpo**: wordmark **"SCULPT BROW"** em dourado, impresso **verticalmente** ao longo do corpo (lê de baixo pra cima). Logo **LF** dourado (monograma, mesma família visual do LF PRO) abaixo do wordmark, menor.
4. **Anel identificador de tom**: uma faixa/anel fino na cor do tom (marrom claro/médio/escuro conforme o SKU) próximo à base do corpo, logo acima da ponta retrátil — é o principal indicador visual de qual tom é, já que não há texto do nome do tom impresso.
5. **Tampa**: separada, formato cilíndrico com topo levemente arredondado/cúpula, preta glossy, sem impressão visível.
6. Sem sangria de cor no corpo principal — só o anel identificador na base.

**Não confirmado ainda:** dimensões exatas (comprimento/diâmetro) — sem foto de escala real (tipo "produto na mão") como temos pro Essential Lips. Pedir ao time antes de travar still com mão/modelo.

### Regra — fundo padrão

Sem sessão de campanha própria ainda rodada nesta pasta — **seguir o padrão geral da marca** (`brand-dna/00-brand-dna.md`): preto/charcoal dark-feed pra vídeo social, off-white pra still tipo e-commerce. Perguntar ao time antes de travar um default específico pra esta linha, diferente do que foi feito com Essential Lips (onde o time pediu preto sólido como padrão único).

## Cartela de tons

| Tom | Descrição oficial | Undertone | Indicado para |
|-----|--------------------|-----------|----------------|
| Light | Marrom claro | Subtom frio | Fios loiros, castanho claro, ruivos, baixo contraste |
| Medium | Marrom médio | Subtom frio | Fios castanho médio, morenos, médio contraste |
| Dark | Marrom profundo acinzentado | Subtom frio | Fios castanho escuro, pretos, alto contraste |

## Fórmula / diferenciais

- **Fórmula anidra** (sem água) — "clean beauty": 100% vegana, sem fragrância, sem conservantes. Sem água na composição garante maior estabilidade, durabilidade e resistência ao longo do dia.
- **Óleo de Mamona**: hidrata e nutre os fios, garantindo maciez e conforto durante o uso.
- **Vitamina E**: ação antioxidante, protege os fios e a pele da sobrancelha do ressecamento.
- **Vitamina C** (confirmado na página de venda, não estava no material de lançamento original): protege a fórmula e os fios sem ressecar.

## Preço e link (confirmado — página de venda, 03/09)

R$ 89,90 (à vista/1x sem juros) — mesmo preço nos 3 tons. Páginas: `lfpro.com.br/products/sculpt-brow-{light,medium,dark}`.

**Catálogo JSON:** os 3 SKUs já foram adicionados em `assets/catalog/{families,products-index,products-full,claims-slim,download-manifest}.json`, no mesmo formato dos outros 91 SKUs — mas com `id`/`sku` do Shopify como `null` (não confirmados; o site está bloqueado pra fetch automático nesta sessão) e imagens apontando pro packshot local do repo, não pro CDN Shopify real. Cada entrada tem um campo `_note` explicando isso. Atualizar com os IDs reais quando o time tiver acesso ao admin do Shopify ou puder colar o JSON do produto.

## Claims de performance (oficiais — confirmado pelo time)

✓ Super macia · ✓ Desliza facilmente · ✓ Não puxa os fios · ✓ Esfuma com facilidade · ✓ Resistente à água · ✓ Resistente à oleosidade · ✓ Não transfere · ✓ Acabamento matte natural

Claims confirmados como oficiais pelo time (03/09) — usar como estão em qualquer peça de comunicação desta linha, sem necessidade da ressalva/guardrail que existe pro Essential Lips.

## Anti-patterns

- Nome do tom errado na ponta (a identificação é só pelo anel de cor na base — não inventar texto de tom no corpo)
- Logo "SCULPT BROW" horizontal ou em posição diferente do vertical real
- Corpo grosso tipo lápis de colorir — é fino, tipo lapiseira de precisão
- Ponta redonda/cônica tradicional — é **chanfrada** (bisel), característica central do produto
- Claims de performance sem ressalva até confirmar substanciação (ver seção acima)
