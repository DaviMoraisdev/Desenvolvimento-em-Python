gamesSet = {"Resident Evil 4", "Star Wars Jedi: Survivor", "Hogwarts Legacy",
              "The Legend of Zelda: Tears of the Kingdom", "God of War Ragnarok"} 
print(gamesSet)

# Não possibilita adicionar valores, remover ou alterar itens do set, pois é imutável.
# Buscar o tamanho do set
print(len(gamesSet))

# True e 1 são iguais 
exampleSet = {1, 2, 3, 4, 5, True}
print(exampleSet)

# Adicionar item de outro set 
gamesSet.update(exampleSet)
print(gamesSet)

# Remover um item do set
gamesSet.remove("Hogwarts Legacy")
print(gamesSet)