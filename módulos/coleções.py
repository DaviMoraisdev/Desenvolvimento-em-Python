from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista 
fruits = ["Maça", "Banana", "Uva", 
           "Uva", "Maça", "Laranja", "Abacaxi",
           "Tangerina", "Uva", "Pêra", "Banana"]
print(fruits)
print(Counter(fruits))

# 2 - Tupla Nomeada 
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Fifa15", 90.5, 8.5)
g2 = game("Resident Evil Requiem", 300, 10.0)
print(g1)
print(g2)

# 3 - Ordenando dicionarios
studants = {"Pedro":23, "Maria":20, "Messi":39}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)

# 4 - Utilizando fila ambas as extremidades 
deq = deque ([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)