import tkinter as tk
from tkinter import ttk
from time import sleep

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
    
    def crear_ventana(self):    
        self.geometry('800x600')
        self.title('Ejemplo proress bar')
        self.__crear_frame()
        self.mainloop()

    def __crear_frame(self):
        frame = ttk.Notebook(self)
        tab = ttk.Frame(frame)
        self.__crear_progress_bar(tab)
        self.__crear_boton_ejecutar(tab)
        self.__crear_boton_ciclo(tab)
        self.__crear_boton_detener(tab)
        self.__crear_boton_despues(tab)
        frame.add(tab, text='Progress bar')
        frame.pack(fill=tk.BOTH)

    def __crear_progress_bar(self, tab):
        self.barra = ttk.Progressbar(tab, orient=tk.HORIZONTAL, length=750)
        self.barra.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
    
    def __iniciar_barra(self):
        self.barra['maximum'] = 100
        for i in range(101):
            sleep(0.1)
            self.barra['value'] = i
            self.barra.update()
        self.barra['value'] = 0

    def __ciclo_barra(self):
        self.barra.start()

    def __detener_barra(self):
        self.barra.stop()

    def __detener_barra_despues(self):
        espera = 2000  # tiempo en ms
        self.after(espera, self.barra.stop())

    def __crear_boton_ejecutar(self, tab):
        boton_inicio = ttk.Button(tab, text='Iniciar', command=self.__iniciar_barra)
        boton_inicio.grid(row=1, column=0, padx=5, pady=5)
    
    def __crear_boton_ciclo(self, tab):
        boton_ciclo = ttk.Button(tab, text='Ciclo', command=self.__ciclo_barra)
        boton_ciclo.grid(row=1, column=1, padx=5, pady=5)
    
    def __crear_boton_detener(self, tab):
        boton_detener = ttk.Button(tab, text='Detener', command=self.__detener_barra)
        boton_detener.grid(row=1, column=2, padx=5, pady=5)

    def __crear_boton_despues(self, tab):
        boton_despues = ttk.Button(tab, text='Boton despues', command=self.__detener_barra_despues)
        boton_despues.grid(row=1, column=3, padx=5, pady=5)

ventana = Ventana()
ventana.crear_ventana()
