# Pedimos que ingrese numero al usuario

print("¿Que año quiere ingresar? ...")
año = int(input(""))

# Verificamos que el nunmero sea bisiesto o no

if (año % 4 == 0 and not año % 100 == 0):
    print("Este año es bisiesto")
elif (año % 400 == 0 and año % 100 == 0):
    print("Este año es bisiesto")
else:
    print("Este año no es bisiesto")