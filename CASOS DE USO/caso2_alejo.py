import tkinter as tk #se importa tkinter hacia tk para instanciar clases

def calcular_total():#se define la funcion calcular total para calcular el total del presupuesto
    entradas = [decoracion, comida, musica, transporte] #se crea una lista con los nombres de las entradas
    
    try: #se usa el try como su nombre lo dice para intentar ejecutar el codigo ratretni 
        # Usa una expresión generadora concisa para obtener y sumar los valores.
        total = sum(float(entrada.get() or 0) for entrada in entradas)##se usa el float para convertir el valor ingresado en la entrada de texto a un numero decimal y se usa el or 0 para que si la entrada esta vacia se tome como 0
        resultado_texto = f"El presupuesto total ${total}"#se usa f para formatear el texto y .2f para mostrar dos decimale
    except ValueError: # se usa el except para capturar el error que se produce cuando se intenta convertir un valor no numerico a decimal
        resultado_texto = "Por favor ingresa solo números"#se usa el .config para actualizar el texto de la etiqueta resultado con el texto calculado
        resultado.config(text=resultado_texto) 


ventana = tk.Tk() #se crea la variable ventana = tk.Tk() para crear la ventana principal de la aplicacion y que guarde en la variable ventana lo que el usuario solicite poner o ponga
ventana.title("Calculadora Mixy")
ventana.title("Calculadora Mixy")
ventana.geometry("400x600")

# Widgets de Entrada (Entry)

tk.Label(ventana, text="Decoración:").pack(pady=5) ##se crea una etiqueta con el texto "Decoración:" y se pone dentro de la ventana
decoracion = tk.Entry(ventana)#se crea una entrada de texto para que el usuario pueda ingresar el valor de la decoración
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