import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext


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

def crear_componentes_tab_2(tabulador):
    contenido = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vel aliquet risus. Donec placerat volutpat velit sit amet pellentesque. Duis mollis, risus at gravida sodales, sem libero aliquam metus, volutpat tincidunt turpis urna nec sapien. Vestibulum a ipsum sit amet lacus hendrerit euismod. In et elementum urna. Sed quis molestie metus. Etiam consequat nisi nunc. Donec non pharetra justo, suscipit consequat augue. Nunc mollis rutrum orci et convallis. Nam vel vestibulum tortor. Vivamus feugiat vehicula dignissim. Mauris fringilla ultrices mi vel cursus. Duis feugiat consectetur neque et ultrices. Suspendisse finibus bibendum vehicula. Quisque ac sem cursus, bibendum arcu in, sagittis est. Vivamus ac risus lacus.
Donec in faucibus lectus. Sed molestie, tortor sed aliquet ultrices, nulla ipsum lacinia arcu, sit amet ornare ipsum magna egestas tellus. Curabitur lacinia tortor in efficitur facilisis. Phasellus ut tincidunt tellus. Fusce malesuada arcu eget dolor aliquet sollicitudin. Donec libero ex, imperdiet ac maximus eget, consectetur non turpis. Morbi vel elit eget dolor aliquam vehicula. Praesent egestas commodo est, eu placerat libero tristique vitae. Maecenas euismod sem risus, ac sagittis sem cursus eget.
In a dictum nisi. Praesent blandit lorem tincidunt viverra semper. Nam varius tortor nibh, eget aliquet leo vehicula vitae. Proin tincidunt augue nec ipsum finibus tincidunt. Aenean sed libero fringilla, maximus lectus nec, pharetra ante. Aliquam erat volutpat. Vivamus vel libero eget justo mollis dapibus. Aenean fringilla lacus sed faucibus sollicitudin. Mauris nec nulla sollicitudin, fringilla eros eget, viverra tortor. Etiam condimentum faucibus suscipit.
Maecenas eu ipsum sit amet diam scelerisque porttitor. Curabitur vitae porttitor eros. Proin vel efficitur lectus. Quisque laoreet at metus id fringilla. Aliquam egestas commodo sem sed ullamcorper. Suspendisse feugiat lacus nec nisl finibus tristique. Curabitur ultricies ullamcorper est cursus cursus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Mauris sit amet imperdiet eros, in mollis erat. Phasellus sagittis dapibus leo sed vestibulum. Nullam tempor arcu ligula. Nulla sit amet tellus nisi. Curabitur vulputate dignissim blandit. Pellentesque imperdiet nunc vel laoreet interdum. Nulla iaculis mauris vel eros mollis, id molestie mauris molestie.
Donec vulputate justo sed ipsum euismod efficitur. Vivamus a egestas nunc. Praesent suscipit commodo rutrum. Etiam vulputate nisi ac turpis scelerisque mollis. Integer sodales quam orci, congue imperdiet lorem cursus vel. Quisque finibus nisl eu quam vulputate mattis. Maecenas sed vestibulum nibh. Vivamus non condimentum risus. Ut sed rutrum nunc. Aliquam a malesuada mi. Aenean ornare finibus odio id pharetra. Mauris suscipit dolor a semper pharetra. Praesent vehicula luctus neque, sit amet dignissim arcu sodales non. 
    '''
    scroll = scrolledtext.ScrolledText(tabulador, width=50, wrap=tk.WORD)
    '''
    width / height = Cantidad de caracteres a mostrar
    '''
    scroll.insert(tk.INSERT, contenido)
    scroll.grid(row=0, column=0)

def crear_tabs():
    control_tabulador = ttk.Notebook(ventana)
    tabulador1 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador1, text='tabulador 1')
    control_tabulador.pack(fill='both')
    crear_componentes_tab_1(tabulador1)

    tabulador2 = ttk.LabelFrame(control_tabulador, text='Contenido')
    control_tabulador.add(tabulador2, text='Tabulador 2')
    crear_componentes_tab_2(tabulador2)
    
ventana = tk.Tk()
ventana.geometry('800x600')
ventana.title('tabs')

crear_tabs()

ventana.mainloop()
