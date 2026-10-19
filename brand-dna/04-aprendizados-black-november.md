# Aprendizados — campanha Black November (out/2026)

Registro de decisões aprovadas/reprovadas pela LF PRO durante a produção das imagens de campanha (fundo preto + fita de cetim preta com escrita dourada). Ler antes de gerar qualquer peça nova da campanha.

## Aprovadas

| Peça | Arquivo | Magnific |
|------|---------|----------|
| 4 paletas 2x2 (Petal, Basic, Sunset, Stone), fita "LF PRO • BLACK NOVEMBER", cores dos pans ajustadas aos packshots | `assets/bases/aprovada-black-november-4-paletas-2x2.png` (4:5) | creation `p8jcBdwehw` (base IA: `Ifw0FlltvE`) |

## Regras que saíram desta campanha

### Formato / composição
- **NÃO ampliar laterais (outpaint / expand / retoque de borda).** A cliente reprova: a emenda entre a área original e a área gerada sempre fica perceptível e as imagens acabam não sendo usadas. Se precisar de outro formato (16:9, 1:1), **gerar a cena já no formato final** com Nano Banana + referências, não expandir uma imagem pronta.
- Fita: texto exato **"LF PRO • BLACK NOVEMBER • LF PRO • BLACK NOVEMBER"** (letras L e F, nunca o monograma no lugar do "LF").
- Fundo sempre preto; luz quente/dourada suave vinda de trás ou de cima-esquerda. Raios de luz / flare = "exagerado" (reprovado).

### Fidelidade de produto
- Paletas novas: estojo preto compacto, quase quadrado, tampa com espelho do mesmo tamanho da base, 6 pans em 2×3. Ordem de cores = `assets/products/paleta-de-sombras-*/01.src.txt` (linha de cima = lado da dobradiça).
- Conferir **posição** de cada pan contra o packshot, não só a cor (Stone já saiu com pans trocados).
- Espelhos de tampa às vezes "refletem" uma segunda paleta inteira → corrigir (reflexo escuro) antes de entregar.
- Não colocar códigos hex no prompt (a IA imprime os códigos como etiqueta). Usar nome das cores + packshot como referência.
- A IA embaralha textos de embalagem (ex.: "BASE UOUIRA", "CONCEALE MOUSSE"). Corrigir com retoque por máscara no Magnific (Nano Banana Pro retouch), com máscara justa só sobre o texto; conferir com zoom antes de entregar.
- Monograma LF nas tampas/lids sai deformado com frequência — sempre conferir com zoom.

### Retoques — SEMPRE perguntar antes
- Antes de qualquer retoque, seja ele pago no Magnific (retouch/edit por máscara) ou feito localmente (reescrever texto de embalagem, recolorir pan, apagar elementos), **perguntar à cliente**. A pergunta deve listar o problema encontrado, o que seria feito, como (Magnific ou local) e quanto custa.
- Fluxo: gerar → conferir → entregar a imagem gerada + lista de problemas → **aguardar OK** → retocar.

### Créditos (MCP — o ilimitado do plano NÃO vale para gerações via MCP)
| Operação | Custo |
|----------|-------|
| Nano Banana Pro 2k (`imagen-nano-banana-2`) | 75 |
| Retouch Nano Banana Pro 2k | 75 (4k = 150 — evitar) |
| Retouch Pro (precise) | 50 — copia/inventa texto em fitas novas |
| Ideogram 4.5 preciseEdit | 80 — não aplicou correções de texto (evitar) |
| Expand (Ideogram) | 50 — resultado inútil (evitar) |
| Uploads | grátis |

- Sempre informar custo + link Magnific em cada entrega.
- Preferir 1 geração bem referenciada (packshots + imagem aprovada como âncora de estilo) a várias tentativas.
- Ajustes de cor de pans podem ser feitos localmente (grátis) sem alterar forma/luz.
