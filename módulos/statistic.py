import statistics

# 1 - Aplicar a média
print(statistics.mean([3, 4, 6, 4, 9]))

# 2 - Aplicar a mediana
print(statistics.median([1, 2, 4, 8, 9, 10]))

# 3 - Aplicar a moda
print(statistics.mode([2, 5, 7, 8, 9, 2, 8, 4, 8, 9, 21, 2, 7, 8, 9, 8]))

# 4 - Desvio padrão 
"""
- Quanto mais próximo de 0 for o desvio padrão,
significa que os dados do conjunto estão menos dispersos 
"""
print(statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5]))