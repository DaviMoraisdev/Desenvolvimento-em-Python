def contar_letras(texto: str) -> int:
    contador = 0
    for letra in texto:
        if (letra.isalpha()): contador += 1

    return contador

print(contar_letras("olá"))


def eh_par(numero: int) -> bool:
    """Verifica se o número é par."""
    return numero % 2 == 0

def filtra_pares(numeros: list) -> list:
    return [numero for numero in numeros if eh_par(numero)]

def filtra_impares(numeros: list) -> list:
    return [numero for numero in numeros  if not eh_par(numero)]

numeros = [1, 2, 3, 4, 5, 8, 5, 6]
print(filtra_pares(numeros))
print(filtra_impares(numeros))

produtos = [
    {"nome": "Notebook", "preco": 2500},
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 150},
    {"nome": "Monitor", "preco": 800}
]

def aplicar_desconto(preco: int, desconto_pct: float = 20.0) -> float:
    preco_reduzido = preco * (1 * desconto_pct / 100)
    return preco_reduzido

produtos_com_desconto = []

for produto in produtos:
    produto_com_desconto = produto
    produto_com_desconto.update({"preço": aplicar_desconto(produto_com_desconto["preco"])})
    produtos_com_desconto.append(produto_com_desconto)

print(produtos_com_desconto)