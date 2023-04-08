import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry('800x600')
ventana.title('componente de mensajes')

def mostrar_texto():
    # messagebox.showinfo('Info', txt.get())
    # messagebox.showerror('Error', txt.get())
    messagebox.showwarning('Advertencia', txt.get())
    txt.delete(0, tk.END)
    txt.focus()

label = ttk.Label(ventana, text='Ingrese un texto')
label.grid(row=0, column=0)

txt = ttk.Entry(ventana, width=30)
txt.grid(row=1, column=0)
txt.focus()

boton = ttk.Button(ventana, text='Mostrar', command=mostrar_texto)
boton.grid(row=2, column=0, pady=10)

ventana.mainloop()
