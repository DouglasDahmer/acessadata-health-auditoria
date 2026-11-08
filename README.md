# AcessaData-Health · Auditoria computacional 2015–2024

**Entregas 01 e 02 — auditoria computacional e análise epidemiológica.**

Projeto técnico de análise de mortalidade por neoplasias malignas (CID-10 C00–C97) em residentes do Rio Grande do Sul (RS), com base no SIM e projeções populacionais do IBGE.

> **Estado:** relatório preliminar. Esta publicação apresenta **resultados agregados e verificações demonstrativas**; não divulga microdados individuais nem substitui revisão científica externa.

## Indicadores da pesquisa

| Indicador | Resultado |
|---|---:|
| Óbitos totais no recorte, 2015–2024 | 194.368 |
| Óbitos classificados | 194.349 |
| Diferença conciliada | 19 |
| Estratos usados nas análises | 380 |
| Verificações AdVeri na auditoria local | 4/4 |
| Confronto TabNet 2022 | 20.234 = 20.234 |
| Confronto TabNet 2023 | 20.291 = 20.291 |

## A publicação

Esta pasta é um **projeto Quarto**. O HTML gerado reúne explicações, tabelas e visualizações, com código R inspecionável.

- `index.qmd`: introdução e escopo.
- `auditoria.qmd`: conciliação anual e confronto TabNet.
- `tendencias.qmd`: resultados CR2 e suas limitações.
- `analise_epidemiologica.qmd`: contagens, taxas brutas, padronização etária e interpretação científica.
- `metodologia.qmd`: regras, fontes, escopo e pendências.
- `reproducibilidade.qmd`: instruções para os testes públicos.
- `dados_publicos/`: **somente tabelas agregadas**.
- `scripts/`: verificadores adicionais em R e Python para as tabelas públicas.

## Testes e renderização local

No PowerShell aberto na raiz desta pasta:

```powershell
Rscript .\scripts\verificar_agregados.R
python .\scripts\verificar_agregados.py
quarto render
New-Item -ItemType File -Path .\docs\.nojekyll -Force | Out-Null
```

Pré-requisitos: Quarto CLI, R com `knitr` e Python. `quarto render` escreve o site em `docs/`.

## GitHub Pages

**Use um repositório público novo, separado do repositório local de pesquisa.** Execute `git status --short` e inspecione todos os arquivos antes de publicar. No GitHub: **Settings → Pages → Deploy from a branch → main /docs**.

Para orientações completas, consulte [`PUBLICACAO.md`](PUBLICACAO.md).

## Limites metodológicos

- SHA-256 confirma a identidade dos **arquivos locais** contra o manifesto, mas não sua identidade com versões remotas posteriores.
- A concordância TabNet em 2022 e 2023 é uma validação cruzada das contagens, sobre o mesmo SIM.
- As posições físicas dos campos dos CSVs sem cabeçalho de 2022–2023 ainda carecem de confirmação documental oficial.
- O resultado inferencial feminino é sensível à especificação da incerteza CR2; somente dez anos distintos estão disponíveis.
- Os scripts deste repositório verificam **tabelas agregadas transcritas da auditoria original**, e não reexecutam o processamento nacional dos microdados.

## Fontes

- [SIM — Ministério da Saúde](https://dadosabertos.saude.gov.br/dataset/sim)
- [DATASUS — Mortalidade pela CID-10](https://datasus.saude.gov.br/mortalidade-desde-1996-pela-cid-10/)
- [IBGE — Projeções da População](https://www.ibge.gov.br/estatisticas/sociais/populacao/9109-projecao-da-populacao.html)

**Autoria da pesquisa:** Douglas Henrique Silveira Dahmer · AcessaData-Health / AcessaData-ONE.
