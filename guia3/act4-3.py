# Definimos variables
cant_c = 0
cant_mj = 0

# Ponemos la condicion con el while
while (cant_c < 15 and cant_mj < 5):
    print("Ingrese el tiempo de esta carrera...")
    tiempo = int(input())
    
    if (tiempo > 12):  # Ponemos condicion para sumar a cant de carreras
        cant_c +=1
    else:              # Si el tiempo es menos a 12 sumarlo a buena carrera
        cant_mj +=1
        cant_c +=1
        
# Cuando se cumple la condicion del while imprime esto en pantalla
print("La sesion ha terminado")