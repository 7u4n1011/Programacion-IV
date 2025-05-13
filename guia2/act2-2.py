# Pedimos los datos

print("¿Cuanto tiene que pagar? ...")
pago = float(input(""))

# Preguntamos en cuantas cuotas quiere pagar

print("¿En cuantas cuotas quiere pagar? ...")
cuotas = int(input(""))

# Calculamos las cuotas

if (1 <= cuotas <= 6):
    total = pago + pago * 0.05
    print(f"Su total a pagar es: {total:.2f}")
elif (7 <= cuotas <= 18):
    total = pago + pago * 0.10
    print(f"Su total a pagar es: {total:.2f}")
elif (cuotas >= 19):
    total = pago + pago * 0.20
    print(f"Su total a pagar es: {total:.2f}")
else:
    print("...")