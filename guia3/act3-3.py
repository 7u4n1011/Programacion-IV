# Importamos la libreria random para utilizarla
import random
intentos = 0
num = 0

# Utilizamos el random
rand = random.randint(1,9)
print(rand)

# Mientras el usuario siga errando e intentos sea menor que 3 se entrará en el while
while num != rand and intentos < 3:
    print("Ingrese un numero entre 1 y 9 para adivinar si es el correcto...")   # Pedimos al usuario que ingrese un numero entre 1 y 9
    num = int(input(""))
    
    if (num == rand):   # Verificamos si acertó
        print("Usted a acertado")
        
    if (num != rand):   # Verificamos si el usuario falló
        print(f"Usted a fallado. Cuando llegue a 3 intentos fallidos perderá. Va {intentos:.2f} intentos...")
        intentos = intentos +1

if (intentos == 3):
    print("Usted a acabado sus intentos")