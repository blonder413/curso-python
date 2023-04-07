import tkinter as tk
import os

ruta_archivo = os.path.abspath(__file__)
ruta = os.path.dirname(ruta_archivo)

print(ruta)

ventana = tk.Tk()

ventana.geometry('800x600')
ventana.title('Mi app')
if os.path.isfile(ruta + '/logo.png'):
    icono = tk.PhotoImage(file=ruta + '/logo.png')
    ventana.iconphoto(True, icono)
else:
    print('la imagen no existe')
ventana.mainloop()
