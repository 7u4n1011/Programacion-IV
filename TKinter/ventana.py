import tkinter as tk

root = tk.Tk()
root.title("Heladeria Juanis Gay´s")

# --- Configuración de ventana ---
root.geometry("400x200")           # Tamaño ancho x alto
root.configure(bg="#f7e7a2")       # Fondo color crema

# --- Etiqueta principal ---
etiqueta = tk.Label(
    root,
    text="🍦 Helado de Sambayón Gratis 🍦",
    font=("Arial", 16, "bold"),
    fg="#5a3e1b",        # color del texto
    bg="#f7e7a2"         # mismo que el fondo
)
etiqueta.pack(pady=20)   # Espacio extra arriba y abajo

# --- Botón ---
def cerrar():
    root.destroy()

boton = tk.Button(
    root,
    text="¡Gracias!",
    font=("Arial", 12),
    bg="#d9b38c",
    fg="white",
    activebackground="#b58c64",
    command=cerrar
)
boton.pack(pady=10)

# --- Pie de página ---
footer = tk.Label(
    root,
    text="Promoción válida hasta agotar stock",
    font=("Arial", 9, "italic"),
    fg="gray",
    bg="#f7e7a2"
)
footer.pack(side="bottom", pady=5)

root.mainloop()
