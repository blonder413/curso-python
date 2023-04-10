import tkinter as tk
from tkinter import ttk

class Ventana:
    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.geometry('800x600')
        self.ventana.title('data list')
        self.crear_frame()
        self.ventana.mainloop()

    def crear_frame(self):
        frame1 = ttk.Notebook(self.ventana)
        
        tab1 = ttk.Labelframe(frame1, text='DataList')
        frame1.add(tab1, text='Componente datalist')
        self.crear_combobox(tab1)
        frame1.pack(fill=tk.BOTH)
    
    def crear_combobox(self,frame):
        datos = [x+1 for x in range(10)]
        combobox = ttk.Combobox(frame, width=15, values=datos)
        combobox.current(3)
        combobox.grid(row=0, column=0, padx=10, pady=10)

        def mostrar_texto():
            print(combobox.get())

        boton = ttk.Button(frame, text='Click', command=mostrar_texto)
        boton.grid(row=1, column=0)


ventana = Ventana()
ventana.crear_ventana()
