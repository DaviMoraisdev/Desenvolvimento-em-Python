import pprint
gamesDict = { 
    " Resident Evil 4": {
        "yearLaunch": 2005,
        "classification" : 9.8,
        "genre" : [ "Action, Adventure, Horror" ]
    },
    "The Last of Us": {
        "yearLaunch": 2013,
        "classification" : 9.5,
        "genre" : [ "Action, Adventure, Drama" ]
    },
    "God of War": {
        "yearLaunch": 2018,
        "classification" : 9.7,
        "genre" : [ "Action, Adventure, Fantasy" ]
    },
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

#Buscar valores 
print (gamesDict[" Resident Evil 4"]["yearLaunch"])

# Adicionar novo item 
gamesDict[" Resident Evil 4"]["developer"] = "Capcom"
print (gamesDict[" Resident Evil 4"]["developer"]) 

# Excluir item 
del gamesDict [" Resident Evil 4"]["developer"]
pp.pprint(gamesDict)