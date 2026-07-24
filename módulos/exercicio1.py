"""
* Módulo de Strings
-> Escreva um mófulo em python para tratar algumas strings
e que possua as seguintes funcionalidades: 
1. Inverter uma string de trás pra frente 
2. Retornar apenas letras com índice par 
3. Retornar apenas letras com índice ímpar 
"""

def inverse(string):
    return string[::-1]

def even_characters(string):
    return string[0::2] # 0 2 4 6 8

def  odd_characters(string):
    return string[1::2] # 1 3 5 7 9