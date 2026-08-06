"""
* Avaliação e Média de notas de filmes
Desenvolva novas funcionalidades para complementar o nosso
gerenciamento da classe Filmes. Segue o escopo das funcionalidaddes:

1 - Uma das funcionalidades requeridas é que o usuário posssa realizar a
avaliação de um filme passando uma nota com parâmetro e que essa nota
seja salva no atributo especifico da classe

2 - Assim que uma avaliação for realizada, deve ser incrementado o
total de avaliadores daquele filme. Obs: Considere criar um atributo
específico para esse fim

3 - Para cada filme ter uma nota de avaliação média que consiste
na divisão do total de avaliações pelo total de avaliadores
"""
class Movie:
    def __init__(self, name, yearLaunch, includePlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0

    def __str__(self):
        return f"Filme: {self.name}"

    def technical_sheet(self):
        print("##Dados do filme##")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includePlan}")
        print(f"Avaliação do filme: {self.totalEvaluation}")
        print(f"Duração: {self.durationMinutes} minutos")
        print(f"Total de avaliadores: {self.evaluators}")

    def evaluate(self, note):
        self.totalEvaluation += note # totalEvaluation = totalEvaluation + note
        self.evaluators += 1

    def average(self):
        print(f"Média do filme: {self.name}: {self.totalEvaluation / self.evaluators} \n")

voice = Movie("A silent voice", 2016, False, 130)
avatar = Movie("Avatar", 2009, True, 162)
voice.evaluate(9.5)
voice.evaluate(10.0)
voice.technical_sheet()
voice.average()
avatar.evaluate(8.0)
avatar.evaluate(7.5)
avatar.technical_sheet()
avatar.average()
