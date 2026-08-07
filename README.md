# LF Pro Studio

Fábrica de **vídeo de produto com IA** para a [LF PRO](https://lfpro.com.br).

Pipeline em etapas (agente + verificador), orquestrado com **OpenSquad**, geração via **Magnific**, montagem com **FFmpeg**.

Material de aula: abra [`aula-micro-treinamento.html`](./aula-micro-treinamento.html) no navegador.

---

## O que tem neste repositório

| Pasta / arquivo | Função |
|-----------------|--------|
| `aula-micro-treinamento.html` | Micro treino (site com menu) — EcoUp × LF Pro |
| `brand-dna/` | Regras de marca, modelos Magnific, o que trava e o que varia |
| `products/` | Fichas por família e produto |
| `tracks/` | Tipos de vídeo (T1…T5) |
| `opensquad/` | Agentes, cadeia e configuração do time |
| `pipeline/` | Passos e scripts da V1 |
| `assets/catalog/` | Índice JSON do catálogo |
| `assets/products/` | Fotos oficiais do site (packshots) |
| `output/look-a-final/` | Referência visual do estilo penteadeira escura |

---

## Como começar

### 1. Clonar

```bash
git clone https://github.com/Ecoupdigital/lfpro-studio.git
cd lfpro-studio
```

### 2. Abrir no Claude Code

Abra esta pasta como workspace.

### 3. Conectar o Magnific

```bash
claude mcp add --transport http magnific https://mcp.magnific.com
claude mcp login magnific
```

### 4. Pedir uma execução

Exemplo:

> Herói de produto Soft Eye Claro, estilo penteadeira escura, imagem inicial e final, Kling 3.0, com verificação de logo.

---

## Regras rápidas de marca

**Travado (sempre):** monograma LF, texto LF PRO, forma do pote/tampa, cor do tom do produto.

**Livre (pode mudar):** ambiente, luz, enquadramento, estilo visual, grão, som, cartão final.

Reprova em logo ou pote → **não gera vídeo**.

Detalhe: `brand-dna/02-lock-vs-free.md`.

---

## Stack

- **Orquestração:** OpenSquad (agentes + pontos de checagem)
- **Imagens:** Magnific → Nano Banana
- **Vídeo:** Magnific → Kling 3.0 (padrão atual de custo/qualidade)
- **Montagem:** FFmpeg (9:16, grão, cartão final, áudio)

---

## Contato

Projeto EcoUp × LF Pro · 2026
