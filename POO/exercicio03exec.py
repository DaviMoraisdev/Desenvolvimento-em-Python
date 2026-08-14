from exercicio03 import Viagem

Viagem0 = Viagem("England")
Viagem1 = Viagem("Iceland")
Viagem2 = Viagem("Japan")
Viagem3 = Viagem("California")
Viagem4 = Viagem("Vinland")

print("Finalmente aconteceu, aproveite seu destino")
viajante = input("Qual seu proposito?\n ")
print(f"{viajante} você se tornou alguém melhor, aproveite!"
      '''
        [0] - England
        [1] - Iceland
        [2] - Japan
        [3] - California
        [4] - Vinland
      '''
      )

choice = int(input("Viva da forma certa\n"))
list_viagem = [Viagem0, Viagem1, Viagem2, Viagem3, Viagem4]

for option in list_viagem:
    if choice >= 5:
        print("Aconteceu mesmo, tente novamente")
        break
    else:
        print(f"{viajante} vc irá renascer para {list_viagem[choice].destino} está escrito")
        print("VIVA! VIVA DAVI!")
        break