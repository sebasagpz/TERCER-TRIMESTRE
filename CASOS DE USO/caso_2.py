import tkinter as tk #se importa tkinter hacia tk para instanciar clases

ventana = tk.Tk()
ventana.title("Calculadora Mixy")
ventana.geometry("400x600")

# Widgets de Entrada (Entry)

tk.Label(ventana, text="Decoración:").pack(pady=5)
decoracion = tk.Entry(ventana)
decoracion.pack()

tk.Label(ventana, text="Comida:").pack(pady=5)
comida = tk.Entry(ventana)
comida.pack()

tk.Label(ventana, text="Música:").pack(pady=5)
musica = tk.Entry(ventana)
musica.pack()

tk.Label(ventana, text="Transporte:").pack(pady=5)
transporte = tk.Entry(ventana)
transporte.pack()

def calcular_total():#se define la funcion calcular total para calcular el total del presupuesto
    entradas = [decoracion, comida, musica, transporte]


    try:
        total = sum(float(e.get() or 0) for e in entradas)
        resultado_texto = f"El presupuesto total es ${total}"
    except ValueError:
        resultado_texto = "Por favor ingresa solo números"
    
    resultado.config(text=resultado_texto)

# Botón para calcular, llama a la función `calcular_total`
tk.Button(ventana, text="Calcular total",
          command=calcular_total,
          fg="black").pack(pady=10)

# Etiqueta donde se mostrará el resultado
resultado = tk.Label(ventana, text="Total del presupuesto")
resultado.pack(pady=10)

# Se inicia el bucle principal de la aplicación
resultado.pack(pady=10)

# Se inicia el bucle principal de la aplicación
ventana.mainloop()