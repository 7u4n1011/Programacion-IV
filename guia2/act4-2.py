import math

# Pedimos al usuario los datos necesarios

print("Ingrese el origen del circulo en el plano...")
print("Ingrese el origen en 'X'...")
cX = float(input(""))

print("Ingrese el origen en 'Y'...")
cY = float(input(""))

print("Ingrese el radio del circulo...")
r = float(input(""))

print("Ingrese el origen del punto...")
print("Ingrese 'X'...")
x = float(input(""))

print("Ingrese 'Y'")
y = float(input(""))

# Comenzamos a calcular

cat1 = abs(cX - x)
cat2 = abs(cY - y)
hipo = math.sqrt(cat1**2 + cat2**2)

if (hipo > r):
    print(f"El punto esta fuera del circulo. {hipo:.2f}")
elif (hipo < r):
    print(f"El punto esta dentro del circulo. {hipo:.2f}")
elif (hipo == r):
    print(f"El punto esta dentro del circulo. {hipo:.2f}")