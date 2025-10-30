import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):
    texto = entrada.get().strip()
    if not texto:
        messagebox.showwarning("Vacío", "Escribe una tarea antes de agregar.")
        return
    lista.insert(tk.END, texto)
    entrada.delete(0, tk.END)
    entrada.focus()

def eliminar_seleccionadas(event=None):
    seleccion = lista.curselection()
    if not seleccion:
        messagebox.showinfo("Sin selección", "Selecciona una o más tareas para eliminar.")
        return
    # Borrar desde el final para no desordenar índices
    for i in reversed(seleccion):
        lista.delete(i)

# Ventana
root = tk.Tk()
root.title("Mis Tareas")
root.geometry("380x320")
root.resizable(False, False)

# Entrada + botón agregar
frame_top = tk.Frame(root, padx=10, pady=10)
frame_top.pack(fill="x")

tk.Label(frame_top, text="Nueva tarea:").pack(anchor="w")
entrada = tk.Entry(frame_top)
entrada.pack(side="left", fill="x", expand=True, pady=5)
btn_agregar = tk.Button(frame_top, text="Agregar", command=agregar_tarea)
btn_agregar.pack(side="left", padx=6)

# Listbox con scrollbar
frame_lista = tk.Frame(root, padx=10)
frame_lista.pack(fill="both", expand=True)

scroll = tk.Scrollbar(frame_lista)
scroll.pack(side="right", fill="y")

lista = tk.Listbox(
    frame_lista,
    selectmode=tk.EXTENDED,   # permite seleccionar varias para borrar
    yscrollcommand=scroll.set,
    height=12
)
lista.pack(side="left", fill="both", expand=True)
scroll.config(command=lista.yview)

# Botón eliminar
frame_botones = tk.Frame(root, pady=10)
frame_botones.pack(fill="x")
btn_eliminar = tk.Button(frame_botones, text="Eliminar seleccionadas", command=eliminar_seleccionadas)
btn_eliminar.pack()

# Atajos
entrada.bind("<Return>", agregar_tarea)   # Enter agrega
lista.bind("<Delete>", eliminar_seleccionadas)  # Supr elimina

entrada.focus()
root.mainloop()
