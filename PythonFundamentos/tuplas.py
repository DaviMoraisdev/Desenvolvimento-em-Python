gameTuple = ("Resident Evil 4", "Star Wars Jedi: Survivor", "Hogwarts Legacy",
           "The Legend of Zelda: Tears of the Kingdom", "God of War Ragnarok")
print(gameTuple)
print(type(gameTuple))

# Não possibilita adicionar valores, remover ou alterar itens da tupla, pois é imutável.
# Buscar os dois primeiros itens da tupla
print(gameTuple[:2])

# Buscar o último itens da tupla
print(gameTuple[-1]) 

#Buscar até uma determinada posição
print(gameTuple[:3])

#Buscar de uma posição em diante
print(gameTuple[1:3])

# Recuperar o índice de um item da tupla
print(gameTuple.index("Hogwarts Legacy"))