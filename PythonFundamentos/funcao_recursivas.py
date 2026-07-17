def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num -1))
    
number = int(input("Digite o número para o fatorial\n"))
print(f"O fatorial de {number} é {factorial(number)}")


# 2 - soma total de um número 

def sum_total(num):
    if num == 1:
        return 1
    else:
        return (num + sum_total(num -1))


