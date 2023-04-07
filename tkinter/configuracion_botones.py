import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title = 'Prueba botones'
ventana.geometry('800x600')

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

def evento4():
    boton4.config(text='Presionado', fg='blue', relief=tk.GROOVE, bg='yellow')  # No funciona con elementos creados con ttk

boton1 = ttk.Button(ventana, text='boton 1')
boton1.grid(row=0, column=0, sticky='NSEW')

boton2 = ttk.Button(ventana, text='boton 2')
boton2.grid(row=0, column=1, sticky='NSEW')

boton3 = ttk.Button(ventana, text='boton 3')
boton3.grid(row=1, column=0, sticky='NSEW')

boton4 = tk.Button(ventana, text='boton 4', command=evento4)
boton4.grid(row=1, column=1, sticky='NSEW')

ventana.mainloop()
