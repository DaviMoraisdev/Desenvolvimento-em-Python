from collections.abc import Callable


def dobro(x):
    return x * 2


dobro2 = lambda x: x * 2

print(dobro(4))
print(dobro2(4))

pessoas = [
    {"nome": "Maria", "idade": 25},
    {"nome": "Joao", "idade": 30},
    {"nome": "Noragami", "idade": 20},
]
pessoas.sort(key=lambda p: p["idade"])

print(pessoas)

numeros = [1, 2, 3, 4, 5]

resultado = list(map(lambda x: x * 2, numeros))


def aplicar_operacao(
    a: int,
    b: int,
    operacao: Callable[[int, int], int],
) -> int:
    return operacao(a, b)


resultado_soma = aplicar_operacao(4, 6, lambda num1, num2: num1 + num2)
resultado_multiplicação = aplicar_operacao(4, 6, lambda num1, num2: num1 * num2)

print(resultado_soma)
print(resultado_multiplicação)
