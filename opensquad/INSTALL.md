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

## Rodar

```text
/opensquad run lfpro-studio
```

Briefing mínimo: `handle` + `track` (T1 ou T2).
