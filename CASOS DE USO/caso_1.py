import tkinter as tk #se importa tkinter
#se creo una lista de diccionarios 
lista_productos = [
    {
    "Nombre": "Pollo",  #nombre,precio y cantidad es la clave , el resulytado de ellas es el valor
    
    "Precio": 3000, 
    "Cantidad": 100 
    },

    {"Nombre": "Carne de Rez", 
    "Precio": 2500, 
    "Cantidad": 150},
     
    {"Nombre": "Pasta",
    "Precio": 1000, 
    "Cantidad": 500},
    
    
    {"Nombre": "Arroz", 
    "Precio": 1000, 
    "Cantidad": 100}
]
ventanas=tk.Tk() # se crea una ventana
ventanas.title("Tienda mixy")  #se ´pone de nombre  con el .title el nombre
ventanas.geometry("350x200") #se crea las medidas de la ventana 
def mostrar():
    for producto in lista_productos:
        texto = f"{producto['Nombre']} - ${producto['Precio']} - Cantidad: {producto['Cantidad']}"
        etiqueta = tk.Label(ventanas, text=texto) # define el widget
        etiqueta.pack() # hace visible y posiciona el widget texto

# Botón para mostrar productos
boton = tk.Button(
    ventanas,
    text="Mostrar productos",
    command=mostrar
)
boton.pack(pady=20)
ventanas.mainloop()
