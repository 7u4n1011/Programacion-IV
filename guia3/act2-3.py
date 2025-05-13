# Pedimos al usuario que ingrese el numero
print("Ingrese el numero entero entre 1 y 10 a multiplicar...")
num = int(input(""))

# Verificamos que el numero ingresado sea correcto
if (1 <= num <= 10):
    for i in range (1,11,1):    # Recorremos del 1 al 10
        print(f"{num} x {i} = {num * i}")   # Imprimimos cada multiplicacion
else:
    print("El numero ingresado no se puede utilzar. Ingrese otro...")
    
        