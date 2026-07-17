gamesList = ["The Last of Us", "God of War", "Horizon Zero Dawn", "Red Dead Redemption 2", "Cyberpunk 2077"] 
# 1 - Iterando sobre a lista de jogos e imprimindo cada jogo
for game in gamesList:
    print(game) 

# 2 - Quando a condição for atendida, o Loop será encerrado 
for game in gamesList: 
    if game == "Read Dead Redemption 2":
        break
    print(game)

# Quando a condição for atendida, o Loop vai para a proxima iteração 
for game in gamesList:
    if game == "Read Dead Redemption 2":
        continue
    print(game)


# 4 - Avaliação do jogo 
gameName = input("Digite o nome do jogo: \n")
gameRating = int(input("Digite quantas avaliações deseja fazer do jogo: \n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota do jogo: \n"))
    sum += note 
print(f"A média de avaliações do jogo {gameName} é: {sum/gameRating}")