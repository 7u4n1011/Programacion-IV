import random

def lista_random(n):
    return [random.randint(0,100) for _ in range(n)]

lista1 = lista_random(10)
print(f"Lista de ventas: {lista1}")

ventas_ordenadas = sorted(lista1, reverse = True)
mejores_tres = ventas_ordenadas[:3]
print(f"Tres mejores ventas: {mejores_tres}")

porcentajes = [venta * 0.10 for venta in mejores_tres]
print(f"10% de las tres mejores ventas: {porcentajes}")
