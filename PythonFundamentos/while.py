# 4 - Avaliação do jogo 
gameName = input("Digite o nome do jogo: \n")
qtdRating = 0
totalRating = 0
rating = 0
average = 0

while (rating != -1):
    rating = float(input("Informe a nota do jogo\n"))
    if(rating != -1):
        totalRating += rating # totalrating = totalRating + rating 
        qtdRating += 1 # qtdRating = qtdRating + 1 
        average = totalRating / qtdRating
print (f"Média das avalliações do jogo {gameName} é {average:.2f}")