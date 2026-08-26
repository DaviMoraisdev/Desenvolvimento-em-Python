from collections import Counter
import random

QTD_SORTEIOS = 10

def sortear_e_contar(brindes: list) ->  Counter:
    resultados = [random.choice(brindes) for _ in range(10)]
    return Counter(resultados)

brindes_disponiveis = ["Camiseta", "Caneca", "Adesivo", "Chaveiro"]
sorteio = sortear_e_contar(brindes_disponiveis)
print(dict(sorteio))


## Exercicio 02
import re

padrao = r"\b[A-Z]{2}\d{4}\b"
texto_compras = "Cupom de 20% usado: PY2026. tentei usar o cupom antigo, mas expirou. O novo é WEB9988 e o VIP é vp2026 "

def filtrar_cupons(texto: str) -> list:
    return re.findall(padrao, texto)

print(filtrar_cupons(texto_compras))


## Exercicio 03
import json

dados_alunos = """
[
    {"nome": "Arthur", "tecnologias": ["Python", "JavaScript"]},
    {"nome": "Ana", "tecnologias": ["Java", "C#"]},
    {"nome": "Léo", "tecnologias": ["React", "TypeScript", "Python"]},
    {"nome": "Beatriz", "tecnologias": ["Ruby"]}
]
"""

alunos = json.loads(dados_alunos)

alunos_python =  [aluno["nome"] for aluno in alunos if aluno["tecnologias"]]

print(alunos_python)

