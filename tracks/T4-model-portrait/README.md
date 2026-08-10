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

## Persona e realismo (obrigatório)

- Elenco segue `brand-dna/04-modelos-realismo.md`: idade aparente 30+, elenco cobrindo claro/médio/médio-escuro/escuro.
- `Bea Casting` escolhe o `cast_id` compatível com o tom do SKU antes do still.
- Still/vídeo com rosto passa por **dois** gates antes do Seedance/Kling: `Rita Still Verifier` (packaging/logo, como em T1/T2) **e** `Nina Pele` (identidade, pele, cor de produto). Nenhum vídeo com pessoa sem os dois `APPROVE`.

## Pipeline mental

```
Bea Casting escolhe cast_id → cast anchor (character ref) → still variation (leve)
→ Rita Still Verifier (packaging) + Nina Pele (pele/identidade) → i2v (character-locked) → FFmpeg
product packshot composite se logo no frame falhar
```

Ver `brand-dna/casting-v2.md` e `brand-dna/04-modelos-realismo.md`.
