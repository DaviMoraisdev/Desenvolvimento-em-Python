#Métodos de listas: 
gamesList = ["Resident Evil 4", "Star Wars Jedi: Survivor", "Hogwarts Legacy", "The Legend of Zelda: Tears of the Kingdom"]

#Tamanho da lista
print(len(gamesList))

#Recuperar um item da lista pelo índice 
print(gamesList.index("Hogwarts Legacy"))

#Adicionar um item ao final da lista
gamesList.append("God of War Ragnarok")
print(gamesList)    

# Ordenar a lista 
gamesList.sort()
print(gamesList)

# Copiar os itens de uma lista para outra
newGamesList = gamesList.copy()
newGamesList.remove("God of War Ragnarok")
print(newGamesList)

# Remover todos os itens da lista
newGamesList.clear()
print(newGamesList)
#-----------------------------------------------------------------------------------------------------------------------# 
# # 1 - Buscar os dois primeiros itens da lista 
# print(gamesList[0:2])

# # 2 - Buscar os dois últimos itens da lista
# print(gamesList[-2:]) 

# # 3 - Buscar o ultimo item da lista
# print(gamesList[-1])

# # 4 - Buscar jogos até uma determinada posição
# print(gamesList[:3])

# # 5 - Buscar jogos de uma posição em diante 
# print(gamesList[1:4])



