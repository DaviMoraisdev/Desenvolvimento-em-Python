
### EXERCÍCOS 02 
# # Substituir caractere repetido 
# name = input("Digite o nome do jogo: \n")
# char = name [0].lower()
# new_name = name.replace(char, '$') 
# new_name = char + new_name[1:]
# print (new_name)

# # Troca de caracteres 
# st1 = 'cab'
# st2 = 'zxy'

# new_st1 = st2[:2] + st1[2:]
# new_st2 = st1[:2] + st2[2:]
# print(new_st1)

# EXERCICIOS 03

# distance = float(input("Digite a distância em metros: \n"))
# if distance <= 200: 
#     ticket = 0.50 * distance 
# else: 
#     ticket = 0.45 * distance 
# print(f"O valor da passagem é: R$ {ticket:.2f}")


# salario = float(input("Digite o salário do funcionário: \n"))
# perc_increase = 0.15 

# if salario > 1250:
#     perc_increase = 0.10
# increase = salario * perc_increase 

# print(f"O aumento do salário é: R$ {increase:.2f}")

# Exercícios 04 - Contagem Regressiva 
import winsound 
x = 10 
while x >= 0:
    print(x)
    x -= 1 
winsound.Beep(2500, 500)

# Tabuada 

number = int(input("Tabuada de: \n "))
begin = int(input("DE: \n"))
end = int(input("ATÉ: \n"))

x = begin 

while x <= end:
    print(f"Tabuada de {number} x {x} = {number * x}")
    x = x + 1 