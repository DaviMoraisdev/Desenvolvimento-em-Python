gamesList = {
    "name": "Resident Evil 4",
    "yearLaunch": "2005",
    "gamePrice": "20.99",
    "classification": "18+",
    "genre": "[Action, Horror, Survival]"
}
print(gamesList)
print(len(gamesList))
print(type(gamesList))

# Recuperar um item do dicionário
print(gamesList['genre'])

# Buscar apenas os valores do dicionário
print(gamesList.values())

# Buscar itens do dicionário com chave e valor 
print(gamesList.items())

# Adicionar um item ao dicionário
gamesList['developer'] = "Capcom"
print(gamesList)

# Atualizar um item do dicionário
gamesList.update({"gamePrice": "19.99"})
print(gamesList)    

# Remover um item do dicionário
gamesList.pop("classification")
print(gamesList)