# Pedimos la entrada del usuario

print("Ingrese el primer digito entre 0 y 9")
d1 = int(input(""))
print("Ingrese el segundo digito entre 0 y 9")
d2 = int(input(""))

# Hacemos el calculo para lograr el mayor numero

res1 = d1 * 10 + d2
res2 = d2 * 10 + d1

if (res1 > res2):
    print(f"El mayor numero que se puede lograr es {res1:.2f}")
elif (res2 > res1):
    print(f"El mayor numero que se puede lograr es {res2:.2f}")
else:
    print("No se ha podido lograr ningun numero")