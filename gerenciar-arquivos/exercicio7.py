import csv
from pathlib import Path
from typing import Dict, List


def ler_csv(arquivo: str | Path) -> List[Dict]:
    try:
        with open(arquivo, "r", encoding="utf-8", newline="") as documento:
            linhas = (linha for linha in documento if linha.strip())
            reader = csv.DictReader(linhas)
            return list(reader)
    except FileNotFoundError:
        print(f"Erro: arquivo '{arquivo}' não foi encontrado")
        return []


def calcular_totais(produtos: List[Dict]) -> List[Dict]:
    resultado = [
        {
            **produto,
            "total": float(produto.get("preco") or 0)
            * int(produto.get("quantidade") or 0),
        }
        for produto in produtos
    ]
    return resultado


def escrever_csv(arquivo: str | Path, produtos: List[Dict]) -> None:
    if not produtos:
        print("Nenhum produto para escrever")
        return

    campos = ["nome", "preco", "quantidade", "total"]

    try:
        with open(arquivo, "w", encoding="utf-8", newline="") as documento:
            writer = csv.DictWriter(documento, fieldnames=campos)
            writer.writeheader()
            writer.writerows(produtos)
        print(f"Arquivo '{arquivo}' criado com sucesso")
    except OSError as error:
        print(f"Erro ao escrever o arquivo: {error}")


if __name__ == "__main__":
    diretorio = Path(__file__).resolve().parent
    produtos = ler_csv(diretorio / "produtos.csv")
    produtos_com_totais = calcular_totais(produtos)
    escrever_csv(diretorio / "produtos_com_totais.csv", produtos_com_totais)
