# Definimos una función llamada 'fact' que calcula el factorial de un número
def fact(num):
    resultado = 1  # Inicializamos la variable 'resultado' en 1 (neutro multiplicativo)

    # Recorremos los números del 1 hasta 'num' inclusive
    for i in range(1, num + 1):
        resultado *= i  # Multiplicamos el resultado acumulado por el valor actual de 'i'

    return resultado  # Devolvemos el valor final, que es el factorial de 'num'

# Solicitamos al usuario que ingrese un número
print("Ingrese un número para hacer su factorial")
num1 = int(input(""))  # Convertimos la entrada del usuario a entero y la guardamos en 'num1'

# Llamamos a la función 'fact' con el número ingresado y mostramos el resultado
print(fact(num1))