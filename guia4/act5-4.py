# Función que determina si un número es primo
def primo(num):
    # Un número menor que 2 no puede ser primo
    if num < 2:
        return False
    
    # Itera desde 2 hasta num - 1 para verificar si hay divisores
    for i in range(2, num - 1, 1):
        # Si el número es divisible por algún número en ese rango, no es primo
        if num % i == 0:
            return False
    
    # Si no se encontró ningún divisor, el número es primo
    return True

# Ejemplo de uso
print("Ingrese un número para comprobar si es primo o no...")
num1 = int(input(""))  # Lee un número entero desde la entrada del usuario
print(primo(num1))     # Llama a la función y muestra el resultado

# Dejo una lista de numeros primos para testear el codigo:
# 1 False
# 2 True
# 3 True
# 4 False
# 5 True
# 10 False
# 11 True
# 13 True
# 16 False
