def convertir_nota_a_sistema_americano(nota):
    if not 1 <= nota <= 10:
        return "Nota inválida"

    if nota >= 9:
        return "A"
    elif nota >= 7:
        return "B"
    elif nota == 6:
        return "C"
    elif nota == 5:
        return "D"
    else:
        return "F"

# Ejemplo de uso:
nota = int(input(""))
print(f"La nota {nota} equivale a: {convertir_nota_a_sistema_americano(nota)}")