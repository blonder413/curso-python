import tkinter as tk
from tkinter import ttk
from tkinter import Menu

ventana = tk.Tk()
ventana.geometry('800x600')
ventana.title('Ejemplo de menú')

def crear_menu():
    menu_principal = Menu(ventana)
    # tearoff = False # Evitar que se separe el menú de la interfaz
    sub_menu_archivo = Menu(menu_principal, tearoff=False)
    sub_menu_archivo.add_command(label='Nuevo')
    menu_principal.add_cascade(menu=sub_menu_archivo, label='Archivo')
    ventana.config(menu=menu_principal)

etiqueta = ttk.Label(ventana, text='Mensaje')
etiqueta.grid(row=0, column=0)

boton = ttk.Button(ventana, text='click')
boton.grid(row=1, column=0)

crear_menu()
ventana.mainloop()
