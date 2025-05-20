# Función correcta para el juego del ahorcado
def ahorcado(letra, secret_w):
    resultado = []
    for i in secret_w:
        if i == letra:
            resultado.append(letra)
        else:
            resultado.append('_')
    return resultado

# Probamos la función
palabra = 'ambulancia'
letra_ingresada = 'a'

resul = ahorcado(letra_ingresada, palabra)

print("Palabra secreta:", palabra)
print("Letra ingresada:", letra_ingresada)
print("Resultado:", resul)
