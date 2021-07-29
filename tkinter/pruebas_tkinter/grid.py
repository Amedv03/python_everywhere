import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("650x550")
root.resizable(0, 0)
root.title("solicitud de cheque")

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)



# nombre
nombre_label = ttk.Label(root, text="nombre:")
nombre_label.grid(column=0, row=0,sticky=tk.W, padx=5, pady=5)

nombre_entry = ttk.Entry(root)
nombre_entry.grid(column=0, row=0,sticky=tk.E, padx=5, pady=5)

#cantidad de letras
cantidad_letras = ttk.Label(root, text="Cant. en letras: ")
cantidad_letras.grid(column=0, row=1,sticky=tk.W, padx=5, pady=5)

cantidad_entry = ttk.Entry(root)
cantidad_entry.grid(column=0, row=1,sticky=tk.E, padx=5, pady=5)

#En concepto de
concepto_label = ttk.Label(root, text="Concepto: ")
concepto_label.grid(column=0, row=2,sticky=tk.W, padx=5, pady=5)

concepto_entry = ttk.Entry(root)
concepto_entry.grid(column=0, row=2,sticky=tk.E, padx=5, pady=5)

#Fecha
fecha_label = ttk.Label(root, text="Fecha")
fecha_label.grid(column=1, row=0,sticky=tk.E, padx=5, pady=5)

fecha_entry = ttk.Entry(root)
fecha_entry.grid(column=2, row=0,sticky=tk.W, padx=5, pady=5)

#nombre de la cuenta
nombre_cuenta_label = ttk.Label(root, text="Nombre de la cuenta: ")
nombre_cuenta_label.grid(column=0, row=14,sticky=tk.W, padx=5, pady=5)






root.mainloop()