import random

def lista_random(n):
    return [random.randint(0,100) for _ in range(n)]

lista1 = lista_random(10)

i = 0
while i < len(lista1):
    