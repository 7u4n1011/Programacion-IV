# Pedimos los datos al usuario

print("Ingrese los segundos del primer nadador...")
nadador1 = float(input(""))
print("Ingrese los segundo del segundo nadador...")
nadador2 = float(input(""))
print("Ingrese los segundos del tercer nadador...")
nadador3 = float(input(""))

# Calculamos el podio

if (nadador1 < nadador2 and nadador1 < nadador3):
    primero = nadador1
    if (nadador2 < nadador3):
        segundo = nadador2
        tercero = nadador3
    else:
        segundo = nadador3
        tercero = nadador2
elif (nadador2 < nadador1 and nadador2 < nadador3):
    primero = nadador2
    if (nadador1 < nadador3):
        segundo = nadador1
        tercero = nadador3
    else:
        segundo = nadador3
        tercero = nadador1
else:
    primero = nadador3
    if (nadador1 < nadador2):
        segundo = nadador1
        tercero = nadador2
    else:
        segundo = nadador2
        tercero = nadador1

# Salida por pantalla

print(f"Primer lugar el nadador con {primero:.2f} segundos")
print(f"Segundo lugar el nadador con {segundo:.2f} segundos")
print(f"Tercer lugar el nadador con {tercero:.2f} segundos")