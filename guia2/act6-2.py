#simul=0, mult2=0, mult3=0

# Pedimos los datos al usuario

print("Ingrese el numero natural a calcular...")
natural = int(input(""))

# Calculamos y presentamos por pantalla si es multiplo

if (natural % 2 ==  0 and natural % 3 == 0):
    simul = natural
    print(f"El numero {simul:.2f} es simultaneamente multiplo de 2 y 3")
elif (natural % 2 == 0):
    mult2 = natural
    print(f"El numero {mult2:.2f} es multiplo de 2")
elif (natural % 3 == 0):
    mult3 = natural
    print(f"El numero {mult3:.2f} es multiplo de 3")
else:
    print(f"El numero {natural:.2f} no es multiplo de 2 ni de 3")
