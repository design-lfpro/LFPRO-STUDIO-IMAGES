#!/usr/bin/env python3
"""
Sincroniza produto(s) reais do Shopify público (lfpro.com.br) para o catálogo local.

NÃO precisa de acesso admin/API key do Shopify. Usa o endpoint público que
toda loja Shopify expõe por padrão:

    https://lfpro.com.br/products/{handle}.json

Uso:
    # 1 produto específico, handle exato (confirmar no link real do produto)
    python3 pipeline/scripts/sync_shopify_product.py essential-lips-beige sculpt-brow-light ...

    # descobrir automaticamente todos os handles novos que contenham um termo
    python3 pipeline/scripts/sync_shopify_product.py --discover "essential-lips" "sculpt-brow"

O script:
  1. Busca o JSON público real de cada produto (id, variants, preço, imagens CDN reais).
  2. Faz upsert em assets/catalog/products-full.json e products-index.json
     (mesmo schema dos outros 91 SKUs — não inventa nada, é o dado real).
  3. Baixa as imagens reais do CDN Shopify para assets/products/{handle}/01.png, 02.png...
     (substituindo os packshots provisórios do Drive, se existirem).
  4. Atualiza o front-matter da ficha products/{family}/{handle}.md:
     - url: passa a ser o link real
     - status: remove sufixo "-pre-launch"
     - adiciona shopify_id / sku / price reais

Se este ambiente não tiver acesso de rede a lfpro.com.br (bloqueio de proxy),
rode este script numa máquina com internet normal (ex: Claude Code local,
ou qualquer terminal com Python 3) — não precisa de nenhuma credencial.
"""
import json
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CATALOG_DIR = REPO_ROOT / "assets" / "catalog"
PRODUCTS_DIR = REPO_ROOT / "products"
ASSETS_DIR = REPO_ROOT / "assets" / "products"
BASE_URL = "https://lfpro.com.br"
UA = "Mozilla/5.0 (compatible; LFProStudioCatalogSync/1.0)"


def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def strip_html(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html or "")
    return re.sub(r"\s+", " ", text).strip()


def load_json_list(path: Path):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return []


def save_json_list(path: Path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def upsert_by_handle(items: list, new_item: dict):
    for i, it in enumerate(items):
        if it.get("handle") == new_item["handle"]:
            items[i] = new_item
            return "updated"
    items.append(new_item)
    return "added"


def build_index_entry(full: dict) -> dict:
    return {
        "id": full["id"],
        "handle": full["handle"],
        "title": full["title"],
        "product_type": full.get("product_type", ""),
        "vendor": full.get("vendor", ""),
        "tags": full.get("tags", []),
        "status": "active",
        "variants_count": len(full.get("variants", [])),
        "variants": [
            {
                "id": v["id"],
                "title": v.get("title"),
                "sku": v.get("sku"),
                "option1": v.get("option1"),
                "price": v.get("price"),
                "available": v.get("available"),
            }
            for v in full.get("variants", [])
        ],
        "options": full.get("options", []),
        "images_count": len(full.get("images", [])),
        "images": full.get("images", []),
        "body_text": strip_html(full.get("body_html", "")),
        "url": f"{BASE_URL}/products/{full['handle']}",
    }


def download_images(handle: str, images: list):
    out_dir = ASSETS_DIR / handle
    out_dir.mkdir(parents=True, exist_ok=True)
    for pos, img in enumerate(sorted(images, key=lambda i: i.get("position", 0)), start=1):
        src = img.get("src") or img.get("src_download")
        if not src:
            continue
        ext = src.split("?")[0].rsplit(".", 1)[-1].lower()
        ext = ext if ext in ("png", "jpg", "jpeg", "webp") else "png"
        target = out_dir / f"{pos:02d}.{ext}"
        try:
            data = fetch_bytes(src)
            target.write_bytes(data)
            (out_dir / f"{pos:02d}.src.txt").write_text(src + "\n", encoding="utf-8")
            print(f"  imagem {pos:02d}.{ext} ({len(data)} bytes) <- {src}")
        except Exception as e:
            print(f"  [AVISO] falha ao baixar imagem {pos}: {e}")


def update_ficha_frontmatter(handle: str, full: dict):
    matches = list(PRODUCTS_DIR.glob(f"*/{handle}.md"))
    if not matches:
        print(f"  [AVISO] nenhuma ficha products/*/{handle}.md encontrada para atualizar front-matter manualmente.")
        return
    ficha = matches[0]
    text = ficha.read_text(encoding="utf-8")
    variant = (full.get("variants") or [{}])[0]
    text = text.replace('url: "pending-launch-2026-09-09"', f'url: "{BASE_URL}/products/{handle}"')
    text = re.sub(r"status: dna-v1-pre-launch", "status: dna-v1", text)
    if "shopify_id:" not in text:
        extra = (
            f"shopify_id: {full['id']}\n"
            f"shopify_sku: \"{variant.get('sku', '')}\"\n"
            f"price_brl: \"{variant.get('price', '')}\"\n"
        )
        text = text.replace("---\n\n#", extra + "---\n\n#", 1) if "---\n\n#" in text else text
        # fallback: insert before the closing '---' of frontmatter (second occurrence)
        if "shopify_id:" not in text:
            parts = text.split("---", 2)
            if len(parts) == 3:
                parts[1] = parts[1].rstrip("\n") + "\n" + extra
                text = "---".join(parts)
    ficha.write_text(text, encoding="utf-8")
    print(f"  ficha atualizada: {ficha.relative_to(REPO_ROOT)}")


def sync_handle(handle: str):
    print(f"\n=== {handle} ===")
    url = f"{BASE_URL}/products/{handle}.json"
    try:
        data = fetch_json(url)
    except urllib.error.HTTPError as e:
        print(f"  [ERRO] {e.code} ao buscar {url} — handle pode estar errado ou produto ainda não publicado.")
        return
    except Exception as e:
        print(f"  [ERRO] falha de rede ao buscar {url}: {e}")
        print("  Se este ambiente bloqueia lfpro.com.br, rode este script numa máquina com internet normal.")
        return

    full = data.get("product", data)  # alguns endpoints retornam {"product": {...}}
    full["handle"] = full.get("handle", handle)

    full_path = CATALOG_DIR / "products-full.json"
    index_path = CATALOG_DIR / "products-index.json"
    full_list = load_json_list(full_path)
    index_list = load_json_list(index_path)

    action = upsert_by_handle(full_list, full)
    index_entry = build_index_entry(full)
    upsert_by_handle(index_list, index_entry)

    save_json_list(full_path, full_list)
    save_json_list(index_path, index_list)
    print(f"  catálogo: {action} em products-full.json / products-index.json ({len(full.get('variants', []))} variante(s))")

    download_images(handle, full.get("images", []))
    update_ficha_frontmatter(handle, full)


def discover(terms: list):
    print(f"Descobrindo produtos contendo: {terms}")
    page = 1
    found = []
    while True:
        url = f"{BASE_URL}/products.json?limit=250&page={page}"
        try:
            data = fetch_json(url)
        except Exception as e:
            print(f"[ERRO] falha ao listar catálogo: {e}")
            break
        products = data.get("products", [])
        if not products:
            break
        for p in products:
            handle = p.get("handle", "")
            title = p.get("title", "")
            if any(t.lower() in handle.lower() or t.lower() in title.lower() for t in terms):
                found.append(handle)
        page += 1
    return found


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    if args[0] == "--discover":
        handles = discover(args[1:])
        print(f"\nEncontrados {len(handles)} handle(s): {handles}")
        for h in handles:
            sync_handle(h)
    else:
        for h in args:
            sync_handle(h)


if __name__ == "__main__":
    main()
