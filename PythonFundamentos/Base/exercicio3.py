# Exercicio 1 - Contagem regressiva 
print("Contagem Regressiva")
for numero in range(10, -1, -1):
    print(numero)
print("Lançamento!")

# Exercicio 2 
numero = int(input("Digite um numero (1-10): "))

if numero > 10 or numero < 1:
    print("Número inválido")
    exit()

print(f"Tabuda do {numero}:")
for i in range(1, 11):
    resultado = numero * 1
    print(f"{i} X {numero} = {resultado}")

# Exercicio 3 - Filtro de dados 
produtos = [
	{"nome": "Mouse", "preco": 50},
	{"nome": "Teclado", "preco": 150},
	{"nome": "Monitor", "preco": 300},
	{"nome": "Webcam", "preco": 80},
	{"nome": "Mousepad", "preco": 30}
]

print("Produtos abaixo de R$ 100: ")

for produto in produtos:
    if produto["preço"] <= 100:
       preco_imposto  = produto["preco"] * 1.1
    print(f" - {produto["nome"]}: R$ {produto["preco"]:.2f} (com imposto: R$ {preco_imposto:.2f})")