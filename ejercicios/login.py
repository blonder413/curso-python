import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x130')
        self.title('ventana de ejemplo de login')
        self.resizable(0,0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
    
        self.__crear_componentes()
        self.mainloop()
    
    def __crear_componentes(self):
        usuario_etiqueta = ttk.Label(self, text='Usuario')
        usuario_etiqueta.grid(row=0, column=0, sticky='E', padx=5, pady=5)

        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.usuario_entrada.focus_force()

        password_etiqueta = ttk.Label(self, text='Password')
        password_etiqueta.grid(row=1, column=0, sticky='E', padx=5, pady=5)

        self.password_entrada = ttk.Entry(self, show='*')
        self.password_entrada.grid(row=1, column=1, sticky='W', padx=5, pady=5)

    
        login_boton = ttk.Button(self, text='login', command=self.__login)
        login_boton.grid(row=2, column=1, columnspan=2)
    
    def __login(self):
        username = self.usuario_entrada.get()
        password = self.password_entrada.get()

        if username == 'blonder413' and password == '123456':
            messagebox.showinfo('Correcto', f'Bienvenido {username}')
        else:
            messagebox.showerror('Error', f'Malvenido {username}')

ventana = Login()
