def somar(a: int, b: int) -> int:
    return a + b

def soamr2(nome, *numeros):
    return sum(numeros)

def criar(**usuario):
    print(usuario)
    for chave, valor in usuario.items():
        print(f" {chave}: {valor}")


criar(idade=21, nome="Arthur")





def funcao_completa(a, b, *args, chave1=10, **kwargs):
    """Função com todos os tipos de comportamentos. """
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"chave1={chave1}")
    print(f"kwargs={kwargs}")

funcao_completa(1, 2, 3, 4, 5, chave1=20, nome="Davi", idade=25)

frutas = ["laranja", "maça", {"abc": 123}]

novas_frutas = [*frutas, "abacaxi"]

novas_frutas[2].update({"def": 456})

print(frutas)
print(novas_frutas)

def exemplo(lista: list):
    lista.append(123)

lista2 = [4, 5, 6]
exemplo(lista2)
print(lista2)