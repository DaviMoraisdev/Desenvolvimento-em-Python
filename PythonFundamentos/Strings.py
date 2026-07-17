'''
# Introdução a Strings no Python: 

gameName = "Fifa 26"
gameName2 = "fifa 26"

print (gameName)
print (gameName2)
print (gameName == gameName2)  ## Python é case sensitive 

# Strings multilinhas para melhor visualização 
gameDescription = """
Fifa 26 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar de forma local ou 
multiplayer
"""
print(gameDescription)

# Operações com String 

gameDescription = """
Fifa 26 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar de forma local ou 
multiplayer
"""
gameName = "Fifa" 
gameVersion = "23"
line = '='
# 1 - Operação de Concatenação de Strings
print (line * 25)
gameFullName = gameName + gameVersion 
print (gameFullName)

# 2 - Multiplicação de Strings 

line = '='
print (line * 25)

# 3 - Procura palavra de um texto 
print ("Fifa" in gameDescription)
print ("futebol" in gameDescription)
'''

## Métodos de String 
gameName = "Fifa 26"

gameDescription = """
Fifa 26 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar de forma local ou 
multiplayer
"""

print (gameName.upper()) # Retornar string em maiusculo 
print (gameName.lower()) # Retorna a string em minusculo 
print (gameName.capitalize()) # Apenas a primeira letra em maiusculo 
print (gameName.title())# Retorna a string centralizada com caractere de preenchimento 
print (gameName.center(10, '-'))# Retorna a string centralizada com caractere de preenchimento 
print (gameName.find("a"))# Retorna a posição de um determinado caractere 
print (gameDescription.count("f"))# Conta caracteres 
print (gameDescription.replace("Fifa", "Pes"))# Altera elementos de texto 
print (gameDescription.split(','))

