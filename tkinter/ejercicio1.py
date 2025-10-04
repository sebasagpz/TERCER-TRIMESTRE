import tkinter as tk
from tkinter import messagebox

# Función para mostrar los datos en un mensaje emergente
def guardar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    correo = entry_correo.get()

    if not nombre or not edad or not correo:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
        return

    try:
        edad_int = int(edad)  # Validar que la edad sea un número
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número.")
        return

    mensaje = f"Nombre: {nombre}\nEdad: {edad_int}\nCorreo: {correo}"
    messagebox.showinfo("Datos guardados", mensaje)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Usuario")
ventana.geometry("300x250")
ventana.config(bg="#f5f5f5")

# Etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:", bg="#f5f5f5")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack()

label_edad = tk.Label(ventana, text="Edad:", bg="#f5f5f5")
label_edad.pack(pady=5)
entry_edad = tk.Entry(ventana, width=30)
entry_edad.pack()

label_correo = tk.Label(ventana, text="Correo:", bg="#f5f5f5")
label_correo.pack(pady=5)
entry_correo = tk.Entry(ventana, width=30)
entry_correo.pack()

# Botón guardar
btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos, bg="#4CAF50", fg="white", width=15)
btn_guardar.pack(pady=20)

# Ejecutar la interfaz
ventana.mainloop()
