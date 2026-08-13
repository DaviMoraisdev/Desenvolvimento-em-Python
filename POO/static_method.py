"""
1 - O método estático não recebe automaticamente a instância ou a classe
2 - O método estático não acessa o estado da instância ou da classe por padrão
3 - Usamos o decorator @staticmethod para criar um método estático
"""


class Language:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail

    @staticmethod
    def courses_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Domínio do Python", "Módulos e Pip", "Orientação a Objetos"]
        elif trail == "Automação com o Python":
            courses = [
                "Automação de tarefas",
                "Web Scraping",
                "Assistente Virtual em Python",
            ]
        else:
            courses = ["A definir"]
        return courses


print(Language.courses_trail("Python Fundamentos"))
print(Language.courses_trail("Análise de Dados"))
