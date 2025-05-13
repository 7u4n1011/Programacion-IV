print("¿Cuanto dinero de donación recibió el hospital?")
donacion = float(input(""))

cardiologia = donacion * 0.30
donacion = donacion - cardiologia

neonatologia = cardiologia * 0.70
donacion = donacion - neonatologia

terapia_intensiva = neonatologia * 0.80
donacion = donacion - terapia_intensiva

administracion = donacion

print(f"Terapia Intensiva recibira: {terapia_intensiva:.2f} pesos de la donacion.")
print(f"Neonatologia recibira: {neonatologia:.2f} pesos de la donacion.")
print(f"Cardiologia recibira: {cardiologia:.2f} pesos de la donacion.")
print(f"Administracion redibira: {administracion:.2f} pesos de la donacion.")