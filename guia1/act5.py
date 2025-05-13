# Defino variable constante
pi = 3.141592653589793

# Pido datos que me pide el enunciado
print("¿Cuanto mide de ancho la parte rectangular de la cancha?")
A_ancho_rectangulo = float(input(""))

print("¿Cuanto mide de largo la parte rectangular de la cancha?")
B_largo_rectangulo = float(input(""))

print("¿Cuanto mide de ancho la pista de atletismo?")
C_ancho_pista = float(input(""))

# Calculando cesped sintetico (1)
area_cancha = A_ancho_rectangulo * B_largo_rectangulo
radio = B_largo_rectangulo / 2
area_cabeceras = radio**2 * pi
pasto = area_cabeceras + area_cancha

# Calculo el area de la superficie de la pista (2)


# Imprimo por pantalla lo correspondiente
print(f"La cantidad a cubrir de pasto sintetico es: {pasto:.2f} metros.")