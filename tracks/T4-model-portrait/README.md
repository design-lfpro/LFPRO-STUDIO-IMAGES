---
track: T4-model-portrait
status: v2-planned
---

# T4 — Model Portrait (V2)

## Job

Modelo de estúdio com produto (holding, ao lado do rosto, clean beauty). **Âncora fotográfica real** do cliente preferida.

## Inputs obrigatórios V2

- `cast_id` + anchors em `assets/cast/`
- Packshot do produto
- Look policy: `clean-skin` | `existing-makeup-from-anchor` (não inventar Soft Matte tom X na pele)

## Não faz

- Before/after de cobertura
- Shade match científico
- Trocar identidade entre models sem aprovação

## Pipeline mental

```
cast anchor → still variation (leve) → i2v micro → FFmpeg
product packshot composite se logo no frame falhar
```

Ver `brand-dna/casting-v2.md`.
