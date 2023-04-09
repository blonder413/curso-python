import tkinter as tk
from tkinter import ttk, messagebox

def crear_componentes_tab_1(tabulador):
    def enviar():
        messagebox.showinfo('Mensaje', entrada1.get())
    
    etiqueta1 = ttk.Label(tabulador, text='Nombre')
    etiqueta1.grid(row=0, column=0, sticky='E')

    entrada1 = ttk.Entry(tabulador, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)
    entrada1.focus_force()

    boton1 = ttk.Button(tabulador, text='enviar', command=enviar)
    boton1.grid(row=1, column=0, columnspan=2)

def crear_tabs():
    control_tabulador = ttk.Notebook(ventana)
    tabulador1 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador1, text='tabulador 1')
    control_tabulador.pack(fill='both')
    crear_componentes_tab_1(tabulador1)

    tabulador2 = ttk.LabelFrame(control_tabulador, text='Contenido')
    control_tabulador.add(tabulador2, text='Tabulador 2')
    
ventana = tk.Tk()
ventana.geometry('800x600')
ventana.title('tabs')

crear_tabs()

ventana.mainloop()
