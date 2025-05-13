import random

def adivinar_numero():
    numero_secreto = random.randint(1000, 9000)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinar el número!")
    print("Debes ingresar un número entre 1000 y 9000.")

    while not adivinado:
        try:
            numero_usuario = int(input("Ingresa tu número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if not 1000 <= numero_usuario <= 9000:
            print("El número debe estar entre 1000 y 9000.")
            continue

        intentos += 1

        if numero_usuario == numero_secreto:
            print("¡Acierto!")
            adivinado = True
        elif numero_usuario > numero_secreto:
            print("Menos")
        else:
            print("Más")

    print(f"Adivinaste en {intentos} intento(s).")

# Para ejecutar el juego
adivinar_numero()
