---
status: setup
updated: 2026-08-06
---

# Magnific MCP — setup LFPro Studio

## Endpoint

```text
https://mcp.magnific.com
```

Transport: **HTTP streamable** · Auth: **OAuth 2.0** (conta Magnific, sem API key no chat)

Docs oficiais: https://docs.magnific.com/modelcontextprotocol

## Claude Code (já adicionado + autenticado)

```bash
claude mcp add --transport http -s user magnific https://mcp.magnific.com
claude mcp login magnific   # feito — Status: ✔ Connected
```

## Grok Build (já adicionado — falta OAuth na TUI)

```bash
# Já rodado:
grok mcp add --transport http magnific https://mcp.magnific.com
```

Ficou em `~/.grok/config.toml`:

```toml
[mcp_servers.magnific]
url = "https://mcp.magnific.com"
enabled = true
```

`grok mcp doctor magnific` sobe o server, mas o handshake falha com **Auth required** até autenticar.

### Autenticar no Grok (você)

Tokens do Claude Code **não** copiam pro Grok (client OAuth diferente). Precisa autorizar de novo:

1. No Grok TUI: digite **`/mcps`**
2. Selecione **magnific**
3. Pressione **`i`** (authenticate OAuth)
4. Browser abre → login Magnific (conta EcoUp) → autorizar
5. Volta no Grok → tecla **`r`** pra refresh da lista
6. Confere:

```bash
grok mcp doctor magnific
# esperado: healthy
```

Tokens ficam em `~/.grok/mcp_credentials.json` (0600).

## Tools úteis pro LFPro Studio V1

| Tool MCP | Uso no pipeline |
|----------|-----------------|
| `images_generate` | Still Nano Banana (frame) |
| `images_models_list` / `images_models_show` | Confirmar slug Nano Banana |
| `video_generate` | Seedance i2v |
| `video_models_list` / `video_models_show` | Confirmar Seedance 1.5 Pro |
| `creations_wait` / `creation_status` | Poll até ready |
| `creations_request_upload` + upload + finalize | Subir packshot como reference |
| `account_balance` | Créditos antes do run |

## Modelos LOCK (projeto)

Ver `brand-dna/01-modelos-magnific.md`:

- Stills → **Nano Banana** (`imagen-nano-banana-2` @ 2k)
- Vídeo → **Seedance 1.5 Pro** (Draft / 720p)

## Conta

Usar a conta EcoUp Premium+ (mesmos créditos do app).
