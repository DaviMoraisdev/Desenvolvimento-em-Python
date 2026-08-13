class Movie:
    platform = "Filmes"
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
        print(f"Plataforma: {Movie.platform}")
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
# Modificando a plataforma 
Movie.platform = "Crunchyroll"
avatar.evaluate(8.0)
avatar.evaluate(7.5)
avatar.technical_sheet()
avatar.average()