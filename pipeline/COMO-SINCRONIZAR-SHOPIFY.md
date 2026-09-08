# Como sincronizar produtos novos com o Shopify (guia permanente)

> Se você esqueceu como fazer isso, é só abrir este arquivo — ou pedir pro Claude Code
> ("lê o guia de sincronização e me ajuda a sincronizar [produto]") que ele segue sozinho.

## Por quê esse passo existe

A sessão do Claude Code **na nuvem** (a que você usa pelo navegador/celular) tem o
acesso a `lfpro.com.br` **bloqueado por política de rede** — não é permissão sua,
é do ambiente. Por isso, pra puxar dado real do site (preço, SKU, imagens oficiais
de um produto recém-lançado), é preciso usar a **máquina local** (o computador fixo
que já está configurado), que tem internet normal.

Isso só é necessário para produtos **novos ou recém-lançados** que ainda não estão
nos arquivos `assets/catalog/*.json`. Produtos que já estão no catálogo não
precisam disso.

## Quando usar este guia

- Um produto novo foi lançado no site e você quer que o catálogo local reconheça ele.
- Você pediu pra uma conversa do Claude Code (nuvem) cadastrar um produto e ela
  avisou que não consegue acessar o site pra confirmar dados reais (preço, SKU, id).

## Passo a passo (na máquina local, com Git Bash)

### 1. Abrir o terminal na pasta certa

Abra o **Git Bash** (procura no menu Iniciar) e rode:

```bash
cd ~/Documents/LFPRO-STUDIO-IMAGES
```

### 2. Buscar as atualizações mais recentes do repositório

```bash
git pull
```

### 3. Rodar a sincronização

Se você sabe o(s) termo(s) do produto (nome, parte do handle):

```bash
python pipeline/scripts/sync_shopify_product.py --discover "nome-do-produto"
```

Exemplo real (Essential Lips e Sculpt Brow):

```bash
python pipeline/scripts/sync_shopify_product.py --discover "essential-lips" "sculpt-brow"
```

Se você já sabe o handle exato (visto na URL do produto, tipo
`lfpro.com.br/products/essential-lips-wine`):

```bash
python pipeline/scripts/sync_shopify_product.py essential-lips-wine
```

**O que esse comando faz sozinho:**
- Busca o produto real no site (dado público, sem senha)
- Atualiza `assets/catalog/products-full.json` e `products-index.json` com id/SKU/preço reais
- Baixa as imagens oficiais do produto
- Atualiza a ficha em `products/{família}/{handle}.md` (tira o aviso de "pré-lançamento")

É seguro rodar mais de uma vez — se o produto ainda não estiver no ar, ele só avisa
erro (404) e não muda nada.

### 4. Salvar e enviar as mudanças (só se algo mudou)

```bash
git add -A
git commit -m "Sync [nome do produto] com dados reais do Shopify"
git push
```

**Se aparecer erro "Please tell me who you are" (só acontece na primeira vez):**

```bash
git config --global user.email "mydesign@lfpro.com.br"
git config --global user.name "LFPRO Design"
```

Depois repita o passo 4.

## Atalho: deixar o Claude Code fazer tudo por você

Em vez de digitar os comandos, você pode simplesmente abrir o Claude Code nessa
pasta (`claude` no Git Bash) e pedir em português, por exemplo:

> "sincroniza o produto essential-lips-wine com o Shopify"

Ele lê este guia (é parte do repositório) e roda os comandos sozinho.

## Se algo der errado

- **"command not found: python" ou "command not found: git"** → feche e reabra o
  Git Bash (o programa foi instalado mas o terminal antigo não reconhece ainda).
- **Erro de rede / não consegue acessar o site** → confirme que a máquina local
  tem internet normal (não é o bloqueio da nuvem, então isso não deveria acontecer
  aqui — se acontecer, é só falta de internet mesmo).
- **Não sei o handle do produto** → use `--discover` com uma palavra do nome, o
  script procura sozinho no catálogo público do site.
