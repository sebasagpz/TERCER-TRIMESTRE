import tkinter as tk

# ---------- Funciones ----------
def sumar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado.set(n1 + n2)
    except ValueError:
        resultado.set("Error")

# ---------- Ventana Principal ----------
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("250x180")

# ---------- Variable ----------
resultado = tk.StringVar()

# ---------- Widgets ----------
tk.Label(ventana, text="Número 1:").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2:").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="SUMA", command=sumar).pack(pady=10)

tk.Label(ventana, text="Resultado:").pack()
tk.Label(ventana, textvariable=resultado, fg="blue").pack()

# ---------- Loop Principal ----------
ventana.mainloop()
