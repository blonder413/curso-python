"""
Validar si funciona probando desde la raiz
"""
from tkinter import Tk
from tkinter import Label
from pathlib import Path
import os

ventana = Tk()

ruta_icono = os.path.abspath("./imagenes/logo.ico")

Wpath = Path('logo.ico').absolute()
Upath = Path('logo.xbm').absolute()

if "nt" == os.name:
    if not os.path.isfile(ruta_icono):
        ruta_icono=os.path.abspath("./tkinter/imagenes/logo.ico")
    ventana.wm_iconbitmap(ruta_icono)
    texto = Label(ventana, text=Wpath)
    texto.pack()
else:
    ventana.wm_iconbitmap(bitmap="@imagenes/logo.xbm")
    texto = Label(ventana, text=Upath)
    texto.pack()

ventana.mainloop()
