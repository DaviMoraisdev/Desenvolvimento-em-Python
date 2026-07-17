def wellcome():
    print("Bem-vindo ao curso de Python!")

wellcome()

def sum_values():
    #print(5 + 4)
    return 5 + 4

print(sum_values())

def create_game():
    name = input("Digite o nome do jogo: \n")
    yearLaunch = int(input("Digite o ano de lançamenbto do jogo\n"))
    gamePrice = float(input("Digite o preço do jogo: \n"))
    noteRating = float(input("Digite a nota do jogo: \n"))

    print(f"{name} - R$ {gamePrice}")

create_game()
create_game()


# 1 - crie uma função que receba dois argumento: o primeiro nome eo segundo nome 

def full_name(fname, lname):
    print(f"Nome completo: {fname} {lname}")

full_name("Davi", "Silva")

# 2 - crie uma função que some dois números via parametros

def sum(a, b):
    return a + b

print(sum(10, 50))

#3 - Argumentos default numa função 
def address(country="Brasil"):
    print(f"Eu moro no {country}")

address()
address("EUA")

# 4 - Avaliação do jogo 
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo: \n")
    sum = 0
    for i in range(qtdRating):
        note = float(input(f"Média de avaliação do jogo {game_name} é : {sum / qtdRating}"))

rating_game(2)