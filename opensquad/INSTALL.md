# Instalar / atualizar squad no OpenSquad

## VPS (já copiado)

```text
/home/projects/opensquad/squads/lfpro-studio/
```

## Atualizar a partir do vault (Mac)

```bash
rsync -av --delete \
  ~/vault/01-projetos/lfpro-studio/opensquad/ \
  server-ecoup:/home/projects/opensquad/squads/lfpro-studio/
```

## Dados de marca e packshots

O squad referencia paths relativos ao projeto vault:

```text
~/vault/01-projetos/lfpro-studio/brand-dna/
~/vault/01-projetos/lfpro-studio/products/
~/vault/01-projetos/lfpro-studio/assets/products/
~/vault/01-projetos/lfpro-studio/tracks/
```

Na VPS, se o vault sincroniza em `/home/vault`, usar os mesmos paths absolutos no run.

## Rodar (vídeo — pipeline principal)

```text
/opensquad run lfpro-studio
```

Briefing mínimo: `handle` + `track` (T1 ou T2).

## Rodar (texto para social — pipeline de copy)

Mesmo squad, outro pipeline: `pipeline_social_copy` em `squad.yaml` (spec em `pipeline/pipeline-social-copy.yaml`). Entrada pela **Léa Orquestradora**.

Briefing mínimo: `handle` (produto) + `formato` (reels | carrossel | post-unico | stories). `tema` é opcional — se vazio, `Vini Estrategista` sugere pauta.

Detalhe do fluxo: `pipeline/README-social-copy.md`.
