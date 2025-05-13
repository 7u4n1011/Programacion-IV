def calcularalimento (peso_kg):
    alimento_diario = peso_kg * 30
    porcion = alimento_diario / 2
    alimento_mensual = alimento_diario * 31

    return alimento_diario, porcion, alimento_mensual

peso_gato = float(input("¿Cuanto pesa su gato?"))
diario, porcion, mensual = calcularalimento(peso_gato)

print(f"Alimento diario: {diario:.2f} gramos")
print(f"Porción por comida: {porcion:.2f} gramos")
print(f"Alimento necesario para el mes: {mensual:.2f} gramos")