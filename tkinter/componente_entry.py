import tkinter as tk
from tkinter import ttk

def mostrar_texto():
    # label_resultado.config(text=entrada1.get())
    nombre.set(f'El valor que puso fue {nombre.get()}')
    label_resultado.config(text=nombre.get())

def limpiar_texto():
    entrada1.delete(0, tk.END)
    entrada1.focus()
    label_resultado.config(text='')

ventana = tk.Tk()
ventana.geometry('800x600')
ventana.title('ejemplo de entry')

label1 = ttk.Label(ventana, text='Ingrese su nombre')
label1.grid(row=0, column=0)

nombre = tk.StringVar(value='blonder413')
entrada1 = ttk.Entry(ventana, width=30, justify=tk.LEFT, textvariable=nombre) # width: Cantidad de caracteres
entrada1.grid(row=1, column=0)
entrada1.focus_force()

label2 = ttk.Label(ventana, text='Ingrese su contraseña')
label2.grid(row=0, column=1)

# entrada2 = ttk.Entry(ventana, width=30, show='*', state=tk.DISABLED)
entrada2 = ttk.Entry(ventana, width=30, show='*', state=tk.NORMAL)
entrada2.insert(0, '12345')
entrada2.config(state='readonly')
entrada2.grid(row=1, column=1)

boton1 = ttk.Button(ventana, text='Mostrar', command=mostrar_texto)
boton1.grid(row=2, column=0, padx=10, pady=10, sticky='EW')

boton2= ttk.Button(ventana, text='Limpiar', command=limpiar_texto)
boton2.grid(row=2, column=1)

label_resultado = ttk.Label(ventana)
label_resultado.grid(row=3, column=0, columnspan=2)

ventana.mainloop()
