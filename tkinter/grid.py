import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('800x600')
ventana.title('trabajo con grillas')

def evento1():
    boton1.config(text='botón 1 presionado')

def evento2():
    boton2.config(text= 'botón 2 presionado')

boton1 = ttk.Button(ventana, text='Botón 1', command=evento1)
boton1.grid(row= 0, column= 0)

boton2 = ttk.Button(ventana, text= 'Botón 2', command= evento2)
boton2.grid(row= 1, column= 0)

ventana.mainloop()
