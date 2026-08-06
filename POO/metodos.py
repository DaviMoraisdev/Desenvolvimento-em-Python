class Movie:
    def __init__(self, name, yearLaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"Filme: {self.name}"

    def techinical_sheet(self):
        print("##Dados do filme##")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includePlan}")
        print(f"Avaliação do filme: {self.note}")
        print(f"Duração: {self.durationMinutes} minutos")

mario = Movie("A silent voice", 2016, False, 10, 130)
top_gun = Movie("Top Gun: Maverick", 2022, True, 8, 160)
mario.techinical_sheet()
top_gun.techinical_sheet()
