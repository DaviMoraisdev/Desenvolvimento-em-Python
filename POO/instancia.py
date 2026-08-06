class Movie:
    name = ""
    yearLaunch = 0
    includePlan = False
    note = 0
    durationMinutes = 0

# Primeiro Filme #
movie = Movie()
movie.name = "A silent voice"
movie.yearLaunch = 2016
movie.includePlan = False
movie.note = 10
movie.durationMinutes = 130



print("##Dados do Filme##")
print(f"Nome do filme: {movie.name} \n Ano de Lançamento: {movie.yearLaunch} \n Duração: {movie.durationMinutes} minutos")
