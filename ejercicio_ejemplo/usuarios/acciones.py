from usuarios.usuario import Usuario
import notas.acciones

class Acciones:

    def registro(self):
        print('se va a registrar')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        email = input('Email: ')
        password = input('Contraseña: ')
        usuario = Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(f'{registro[1].nombre} registrado con email {registro[1].email}')
        else:
            print('registro fallido')

    def login(self):
        print('va a iniciar sesión')
        email = input('Email: ')
        password = input('Contraseña: ')
        usuario = Usuario(None, None, email, password)
        login = usuario.identificar()
        if login == None:
            print("No existe usuario con los datos suministrados")
        else:
            print(login)
            self.proximas_acciones(login)

    def proximas_acciones(self, usuario):
        print("""
        Acciones:
        - Crear nota (crear)
        - Mostrar nota (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)
        accion = input("seleccione: ")
        haz_el = notas.acciones.Acciones()

        if accion == "crear":
            haz_el.crear(usuario)
            self.proximas_acciones(usuario)
        elif accion == "mostrar":
            haz_el.mostrar(usuario)
            self.proximas_acciones(usuario)
        elif accion == "eliminar":
            haz_el.borrar(usuario)
            self.proximas_acciones(usuario)
        else:
            exit(0)
