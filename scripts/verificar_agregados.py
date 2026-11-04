"""AcessaData-Health — verificacao demonstrativa das tabelas agregadas."""
import csv
from pathlib import Path

raiz = Path(__file__).resolve().parents[1]

def ler(nome):
    with (raiz / 'dados_publicos' / nome).open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

a = ler('conciliacao_anual.csv')
t = ler('confronto_tabnet.csv')
c = ler('apc_cr2.csv')
esperados = [18094,18409,18979,19085,19665,18960,19579,20234,20291,21072]
assert [int(x['ano']) for x in a] == list(range(2015,2025))
assert [int(x['total']) for x in a] == esperados
assert sum(int(x['total']) for x in a) == 194368
assert sum(int(x['classificados']) for x in a) == 194349
assert sum(int(x['diferenca']) for x in a) == 19
assert all(int(x['total']) - int(x['classificados']) == int(x['diferenca']) for x in a)
assert next(x for x in a if x['ano']=='2022')['diferenca'] == '5'
assert len(t) == 2 and [int(x['ano']) for x in t] == [2022, 2023]
assert all(int(x['sim_local']) == int(x['tabnet']) and int(x['diferenca']) == 0 for x in t)
assert all(int(x['sim_local']) == int(a[int(x['ano'])-2015]['total']) for x in t)
assert len(c) == 4
assert all(float(x['ic_inferior']) < float(x['apc']) < float(x['ic_superior']) for x in c)
print('APROVADO: conciliacao anual 2015-2024')
print('APROVADO: confronto TabNet 2022-2023')
print('APROVADO: estrutura dos quatro resultados CR2 transcritos')
print('ESCOPO: verificacao de tabelas publicas agregadas, sem reprocessar microdados.')
