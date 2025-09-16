import tkinter as tk

def calcular():
    aux = int(edad.get())
    aux *= 7
    e_calculo.config(text = f"La edad humana de tu perro es: {aux}")

root = tk.Tk()
root.title("Calculador")

e_instruccion = tk.Label(root, text = "Cual es la edad de tu perro?")
e_instruccion.grid()

edad = tk.Entry(root)
edad.grid()

b_calcular = tk.Button(root, text = "Calcular", command = calcular)
b_calcular.grid()

e_calculo = tk.Label(root, text = " ")
e_calculo.grid()

root.mainloop()