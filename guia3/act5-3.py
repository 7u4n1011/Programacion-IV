def generar_fibonacci(n):
    if n <= 0:
        print("El número debe ser entero y positivo.")
        return

    fib = []
    a, b = 0, 1

    for _ in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib

# Solicitar al usuario
try:
    n = int(input("Ingrese la cantidad de términos de la sucesión de Fibonacci: "))
    resultado = generar_fibonacci(n)
    if resultado:
        print("Los primeros", n, "números de la sucesión de Fibonacci son:")
        print(" ".join(map(str, resultado)))
except ValueError:
    print("Por favor, ingrese un número entero válido.")