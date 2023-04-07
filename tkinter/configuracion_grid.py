import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('800x600')
ventana.title('Ejemplo de grid')

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

boton1 = ttk.Button(ventana, text= 'Botón 1')
boton2 = ttk.Button(ventana, text= 'Botón 2')
boton3 = ttk.Button(ventana, text= 'Botón 3')
boton4 = ttk.Button(ventana, text= 'Botón 4')

boton1.grid(row=0, column=0, sticky='NSWE')
boton2.grid(row=1, column=0, sticky='NSWE')
boton3.grid(row=0, column=1, sticky='NSWE')
boton4.grid(row=1, column=1, sticky='NSWE')

ventana.mainloop()
