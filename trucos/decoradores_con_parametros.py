def decorador_con_argumentos(funcion):
    def funcion_envolvente(*args, **kwargs):
        print('decorador')
        print(args, kwargs)
        
        # propagar los parámetros a la función original
        return funcion(*args, **kwargs)
    return funcion_envolvente

@decorador_con_argumentos
def saludar(titulo, nombre):
    print(f'Hola {titulo} - {nombre}')

saludar('inge', 'blonder')
