#!/usr/bin/env python3
"""Resolve handle -> local packshot path (01.*)."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCTS = ROOT / "assets" / "products"
INDEX = ROOT / "assets" / "catalog" / "products-index.json"


def resolve(handle: str) -> Path:
    d = PRODUCTS / handle
    if not d.is_dir():
        raise SystemExit(f"missing product dir: {d}")
    for ext in (".png", ".jpg", ".jpeg", ".webp"):
        p = d / f"01{ext}"
        if p.exists():
            return p
    matches = sorted(d.glob("01.*"))
    matches = [m for m in matches if m.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}]
    if not matches:
        raise SystemExit(f"no 01 image for {handle}")
    return matches[0]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("handle")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    path = resolve(args.handle)
    if args.json:
        meta = {}
        if INDEX.exists():
            for p in json.loads(INDEX.read_text()):
                if p["handle"] == args.handle:
                    meta = p
                    break
        print(json.dumps({"handle": args.handle, "packshot": str(path), "title": meta.get("title"), "url": meta.get("url")}, ensure_ascii=False, indent=2))
    else:
        print(path)


if __name__ == "__main__":
    main()
