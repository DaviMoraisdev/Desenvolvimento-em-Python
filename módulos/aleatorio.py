import random

# 1 - Seleciona valor aleatório de uma lista
list1 = [7, 6, 5, 5, 2, 2]
print(random.choice(list1))

# 2 - Gera um némro aleatório em um intervalo de valores 
r1 = random.randint(5, 15)
print(r1)

# 3 - Seleciona caractere aleatorio em um intervalo de valores
name = "Python"
r2 = random.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aleátorio 
#Sintaxe: random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 3))
s = "Olá Mundo"
print(random.sample(s, 2))