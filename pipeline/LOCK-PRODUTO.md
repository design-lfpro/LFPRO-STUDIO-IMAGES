# Trava de produto real — composite-first

**Problema:** gerar o produto com IA (mesmo com o packshot como referência) faz o modelo redesenhar
o formato, o logo e o lettering, e cada tentativa que diverge gasta créditos.

**Regra:** a IA **nunca desenha o produto**. Os pixels do produto vêm sempre do packshot oficial.

## Fluxo

1. **Composite (0 créditos):** `pipeline/scripts/composite_hero.py layout.json out.png`
   - recorta `assets/products/{handle}/01.*` (corpo e tampa viram peças separadas)
   - posiciona, rotaciona e escala cada peça conforme o layout (rascunho do designer)
   - aplica fundo e glow da marca e sombra suave
2. **Aprovação do layout** sobre o composite. Ajustes de posição são feitos no JSON, sem gastar créditos.
3. **Passada IA (re-render 3D comercial):** o composite vira `@img1` com a ordem de não mover nem adicionar nada; os packshots entram como `@img2..n` + bloco PRODUCT LOCK no prompt. Gerar `count: 1` por vez.
   Depois, **recolar o produto original por cima** com a máscara do composite.
   Se a IA alterar o produto, a recolagem desfaz a alteração.
4. **Checagem:** logo e lettering precisam ser idênticos aos do packshot. Pela construção, eles são.

## Limites

- O ângulo é sempre o do packshot (vista frontal), só rotacionado no plano.
  Outro ângulo de câmera exige um packshot novo, fotografado ou fornecido pelo cliente, e não IA.
- A resolução máxima é a do packshot. Escalas acima de ~1.3× perdem nitidez.

## Exemplo

`assets/compositions/intense-eye-hero-black-brown/` (layout.json e v1-composite.png)
