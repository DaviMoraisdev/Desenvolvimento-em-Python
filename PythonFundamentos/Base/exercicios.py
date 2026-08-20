# Exercicio 01 
número = int(input("Digite um número: \n"))
antecessor = número - 1
sucessor = número + 1

print(f"""Número {número}
antecessor: {antecessor}
sucessor: {sucessor}
""")

# Exercicio 02 
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

resultado = (nota1 + nota2 + nota3) / 3
print(f"A média é: {resultado:.2f}")

# Exercicio 03 
nome = "davi"
maiscula = nome.upper()
minuscula = nome.lower()
quantidade = len(nome)
primeras_3 = nome[0:3]
ultimas_3 = nome[-3:]
com_underline = nome.replace(" ", "_")

print(f"nome: {nome}")
print(f"\nMAISCULA: {maiscula}")
print(f"\nminuscula: {minuscula}")
print(f"quantidade: {quantidade}")
print(f"Primeiras 3: {primeras_3}")
print(f"Últimas 3: {ultimas_3}")
print(f"Com underscore: {com_underline}")