"""
* Verificar conteúdo da string
-> Escreva um programa em Python para verificar se uma string
contém apenas um determinado conjunto de caracteres (neste caso, a-z, A-Z E 0-9).
"""

import re

def check_character(string):
    rule = re.compile(r'[^^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)

print(check_character("ASJNDJASDNBSADUSANDUBAUD1825844184284dsdsdadasdada"))
print(check_character("#@^`{};.<>"))