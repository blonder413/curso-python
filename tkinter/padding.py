import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('800x600')
ventana.title('prueba de padding')

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

boton1 = ttk.Button(ventana, text='boton 1')
boton1.grid(row=0, column=0, sticky='NSWE', padx=40, pady=30, ipadx=20, ipady=50, columnspan=2, rowspan=2)

# padx y padx para margen externo
# ipadx y ipady para margen interno

ventana.mainloop()
