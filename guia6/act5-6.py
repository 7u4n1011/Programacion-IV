import random

# Función para generar la matriz aleatoria
def matriz_random(n, m):
    return [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]

# Función para sumar los vecinos de la posición (i, j)
def suma_vecinos(matriz, i, j):
    suma = 0
    filas = len(matriz)
    columnas = len(matriz[0])

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # No sumar la posición central
            ni = i + dx
            nj = j + dy
            if 0 <= ni < filas and 0 <= nj < columnas:
                suma += matriz[ni][nj]
    return suma

# Código principal
n = 5
m = 5

matriz = matriz_random(n, m)

# Mostrar la matriz
print("Matriz generada:")
for fila in matriz:
    print(fila)

# Pedir posición al usuario (ajustando a índice de Python que empieza en 0)
i = int(input(f"Ingrese la fila (1 a {n}): ")) - 1
j = int(input(f"Ingrese la columna (1 a {m}): ")) - 1

# Verificar que la posición ingresada sea válida
if 0 <= i < n and 0 <= j < m:
    resultado = suma_vecinos(matriz, i, j)
    print(f"La suma de los vecinos de la posición ({i+1}, {j+1}) es: {resultado}")
else:
    print("Posición fuera de rango.")
