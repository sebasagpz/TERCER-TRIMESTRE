
import tkinter as tk
from tkinter import ttk, messagebox

# Función de conversión
def convertir():
    try:
        valor = float(entry_valor.get())
        tipo = combo_conversion.get()

        if tipo == "Celsius → Fahrenheit":
            resultado = (valor * 9/5) + 32
            label_resultado.config(text=f"{resultado:.2f} °F")
        elif tipo == "Fahrenheit → Celsius":
            resultado = (valor - 32) * 5/9
            label_resultado.config(text=f"{resultado:.2f} °C")
        else:
            messagebox.showwarning("Selección inválida", "Por favor selecciona un tipo de conversión.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Temperaturas")
ventana.geometry("350x250")
ventana.resizable(False, False)
ventana.config(bg="#f0f0f0")

# Etiqueta
label_titulo = tk.Label(ventana, text="Conversor de Temperatura", font=("Arial", 14, "bold"), bg="#f0f0f0")
label_titulo.pack(pady=10)

# Entrada de valor
label_valor = tk.Label(ventana, text="Ingresa el valor:", bg="#f0f0f0")
label_valor.pack()
entry_valor = tk.Entry(ventana, width=20, justify="center")
entry_valor.pack(pady=5)

# ComboBox para tipo de conversión
label_conversion = tk.Label(ventana, text="Selecciona la conversión:", bg="#f0f0f0")
label_conversion.pack()
combo_conversion = ttk.Combobox(ventana, values=["Celsius → Fahrenheit", "Fahrenheit → Celsius"], state="readonly", width=25)
combo_conversion.pack(pady=5)

# Botón convertir
btn_convertir = tk.Button(ventana, text="Convertir", command=convertir, bg="#4CAF50", fg="white", width=15)
btn_convertir.pack(pady=10)

# Resultado
label_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 12, "bold"), fg="blue", bg="#f0f0f0")
label_resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
