import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('800x600')
ventana.title('Ejemplo con stiky')

def click():
    boton1.config(text= 'hizo click en el botón 1')

boton1 = ttk.Button(ventana, text='Botón 1', command=click)
boton1.grid(row=0, column=0)

boton2 = ttk.Button(ventana, text='botón 2')
boton2.grid(row=1, column=0, sticky='EW')    # Se alinea hacia West (izquierda)

ventana.mainloop()
