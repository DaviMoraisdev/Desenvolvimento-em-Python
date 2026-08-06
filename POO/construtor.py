class Movie:
    def __init__(self, name, yearLaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"Filme: {self.name}"

movie = Movie("A silent voice", 2016, False, 10, 130)
movie2 = Movie("Jujutsu Kaisen 0", 2022, True, 10, 105)
print(movie.name)
print(movie.note)
print(movie2.name)
print(movie2.note)