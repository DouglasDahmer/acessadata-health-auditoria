import csv
import hashlib
import shutil
import tempfile
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from PIL import Image

RAIZ = Path(__file__).resolve().parents[2]

CSV = RAIZ / "dados_publicos" / "series_anuais_sexo_2015_2024.csv"
QMD = RAIZ / "analise_epidemiologica.qmd"

DESTINO = (
    RAIZ / "imagens_fase02"
    / "obitos_classificados_por_sexo_padronizado.png"
)

HASH_ESPERADO = (
    "06fcf2d846e9ec0532a66c8b3bb0e"
    "5c12cac8b4f09f58e3b932ea4bf5f35db97"
)

def sha256(arquivo):
    return hashlib.sha256(arquivo.read_bytes()).hexdigest()

if sha256(CSV) != HASH_ESPERADO:
    raise RuntimeError("CSV diferente do arquivo validado.")

with CSV.open(encoding="utf-8-sig", newline="") as f:
    dados = list(csv.DictReader(f))

assert len(dados) == 20
assert sum(int(r["obitos_classificados"]) for r in dados) == 194349

# Padronizacao fisica: 9 x 4,8 polegadas a 180 DPI.
# Resultado: exatamente 1620 x 864 pixels.

plt.rcParams["font.family"] = "DejaVu Sans"

fig, ax = plt.subplots(figsize=(9, 4.8), dpi=180)

configuracoes = [
    ("Feminino", "#078791", "o", "--"),
    ("Masculino", "#193B57", "s", "-"),
]

for sexo, cor, marcador, estilo in configuracoes:

    serie = sorted(
        [r for r in dados if r["sexo"] == sexo],
        key=lambda r: int(r["ano"])
    )

    assert len(serie) == 10

    ax.plot(
        [int(r["ano"]) for r in serie],
        [int(r["obitos_classificados"]) for r in serie],
        color=cor,
        marker=marcador,
        linestyle=estilo,
        linewidth=2,
        markersize=4,
        label=sexo
    )

ax.set_title(
    "\u00d3bitos por neoplasias malignas \u2014 RS, 2015\u20132024",
    fontsize=12
)

ax.set_xlabel("Ano do \u00f3bito", fontsize=10)
ax.set_ylabel("\u00d3bitos classificados", fontsize=10)

ax.set_ylim(0, 12000)
ax.set_xticks(range(2015, 2025))

ax.grid(axis="y", alpha=0.25)
ax.legend(fontsize=9, loc="upper left")
ax.tick_params(labelsize=9)

fig.subplots_adjust(
    left=0.12,
    right=0.97,
    top=0.89,
    bottom=0.15
)

fig.savefig(
    DESTINO,
    dpi=180,
    facecolor="white"
)

plt.close(fig)

with Image.open(DESTINO) as imagem:
    dimensoes = imagem.size

if dimensoes != (1620, 864):
    raise RuntimeError(f"Dimensoes inesperadas: {dimensoes}")

print("=== GRAFICO PADRONIZADO ===")
print("ARQUIVO:", DESTINO.name)
print("RESOLUCAO:", dimensoes)
print("SHA-256:", sha256(DESTINO))

# Atualiza somente a referencia da primeira imagem.
antigo = "imagens_fase02/obitos_classificados_por_sexo_final.png"
novo = "imagens_fase02/obitos_classificados_por_sexo_padronizado.png"

texto = QMD.read_text(encoding="utf-8-sig")

if antigo in texto:
    backup = (
        Path(tempfile.gettempdir())
        / "acessadata_fase02_qmd_antes_padronizacao.qmd"
    )

    shutil.copy2(QMD, backup)

    texto = texto.replace(antigo, novo)

    nota = (
        "**Fonte e escopo:** SIM / Minist\u00e9rio da "
        "Sa\u00fade; CID-10 C00\u2013C97; residentes do RS. "
        "Os 19 registros n\u00e3o classificados n\u00e3o "
        "integram as s\u00e9ries estratificadas."
    )

    linhas = texto.splitlines(keepends=True)
    resultado = []

    for linha in linhas:
        resultado.append(linha)

        if novo in linha and linha.lstrip().startswith("!["):
            if nota not in texto:
                resultado.append("\n" + nota + "\n\n")

    QMD.write_text("".join(resultado), encoding="utf-8")

elif novo not in texto:
    raise RuntimeError("Referencia da imagem nao encontrada.")

print("PAGINA QMD: ATUALIZADA")
print("DADOS ORIGINAIS: PRESERVADOS")
print("PUBLICACAO REMOTA: NAO EXECUTADA")