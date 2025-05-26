import random

def matriz_random(n,m):
    return [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]

matriz1 = matriz_random(4, 4)

for i in range (len(matriz1)):
    for j in range(len(matriz1[0])):
        if i == j:
            print(matriz1[i][j])