import random

def matriz_random(n,m):
    return [[random.randint(7, 10) for _ in range(m)] for _ in range(n)]

matriz1 = matriz_random(4, 4)

for i in matriz1:
    print(i)

contador = 0
for i in range (len(matriz1)):
    for j in range(len(matriz1[0])):
        if matriz1[i][j] == 9:
            contador += 1

print(f"El numero 9 aparece {contador} veces en la matriz")