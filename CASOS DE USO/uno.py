import tkinter as tk

productos = [
    {"Nombre": "Pollo", "Precio": 3000, "Cant": 200}
]

ventana = tk.Tk()
ventana.geometry("300x250")

def muestra():
    for p in productos:
        texto = f"{p['Nombre']}, {p['Precio']}"
        etiqueta = tk.Label(ventana, text=texto)
        etiqueta.pack()

boton= tk.Button(
ventana,
text = "Mostrar",
command = muestra
)

boton.pack(pady=20)
ventana.mainloop()