import math


def dobro(numero: int) -> int:
    if not isinstance(numero, int):
        raise TypeError("Tipo inválido")
    return numero * 2


def raiz_quadrada(numero: int) -> float:
    return math.sqrt(numero)


if __name__ == "__main__":
    print(dobro(5))
