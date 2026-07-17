"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos 
ter numa função 

- Os argumentos são passados como uma tupla 

**kwargs - Além dos valores podemos passar também as respectivas 
chaves para cada argumento

- Os argumentos são passados como um dicionário

"""
# 1 - soma de números
def sum_numbers(*num):
    sum_total = 0
    for n in num:
        sum_total += n # sum_total = sum_total + n
    print(f"A soma é: {sum_total}")

sum_numbers(7)
sum_numbers(7,9)

# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("###Curso de Python###")
presentation(name="Python", category="Programação", level="Iniciante")
