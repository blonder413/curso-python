import tkinter as tk
from tkinter import ttk, messagebox
import os

ruta_archivo = os.path.dirname(os.path.realpath(__file__))
archivo = os.path.join(ruta_archivo, 'logo.png')


class Ventana:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.geometry('800x600')
        self.ventana.title('Imágenes')
        self.crear_frame()
        self.ventana.mainloop()

    def crear_frame(self):
        frame1 = ttk.Notebook(self.ventana)
        tab1 = ttk.Labelframe(frame1, text='Imágenes')
        self.crear_imagen(tab1)
        frame1.add(tab1, text='manejo de imágenes')
        frame1.pack(fill=tk.BOTH)
    
    def crear_imagen(self, tab):
        imagen = tk.PhotoImage(file=archivo)
        # imagen = imagen.subsample(3)

        def mostrar_informacion_imagen():
            messagebox.showinfo('Informacion', f'{imagen.cget("file")}')

        boton_imagen = ttk.Button(tab, image=imagen, command=mostrar_informacion_imagen) # command es obligatorio para que se muestre la imagen
        boton_imagen.grid(row=0, column=0)

ventana = Ventana()
ventana.crear_ventana()
