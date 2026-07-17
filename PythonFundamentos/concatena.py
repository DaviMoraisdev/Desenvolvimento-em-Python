name =  input("Digite o nome do jogo:\n")
yearLaunch =  int(input("Digite o ano de lançamento do jogo:\n"))
gamePrice = float(input("Digite o preço do jogo:\n"))
planIncluded = input("O plano de assinatura está incluído? (True/False)\n") 

print("###Dados do jogo###")
print("===================")

# #Alternativa 1 
# print("Nome do jogo:", name)
# print("Ano do jogo:", yearLaunch)
# print("Preço do jogo:", gamePrice)
# print("Está incluído no plano?", planIncluded)

#Alternativa 02:
# print("Nome do jogo: ", name, "\n Ano de lançamento: ", yearLaunch, 
#       "\n Preço do jogo:", gamePrice, "\n Está incluso no serviço?", planIncluded)

#Alternativa 03 
print(f"Nome do jogo:{name}\nAno de lançamento:{yearLaunch} \nPreço do jogo: {gamePrice} \nEstá incluso no plano? {planIncluded}")