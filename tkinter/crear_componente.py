import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

ventana.geometry('800x600')
ventana.title('mi app')

def evento_click():
    #boton1.config(text='hizo click')
    # print('hizo click en el botón')
    label = ttk.Label(ventana, text='Hizo click')
    label.pack()

boton1 = ttk.Button(ventana, text='Click aquí', command=evento_click)
boton1.pack()   # Mostrar el componente dentro del layout (ventana)

ventana.mainloop()
