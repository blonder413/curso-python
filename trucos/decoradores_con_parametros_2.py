def decorador_con_argumentos(funcion):
    def funcion_envolvente(*args, **kwargs):
        print('decorador')
        print(args, kwargs)

        # modificar los argumentos antes de enviarlos
        lista = []
        for i, valor in enumerate(args):
            lista.append(valor.upper())
        lista.append('413')

        # agregamos información al diccionario
        # no se puede repetir un indice con *args
        kwargs['nick'] = 'blonder'
        kwargs['edad'] = 30

        # propagar los parámetros modificados
        return funcion(*lista, **kwargs)
    return funcion_envolvente

@decorador_con_argumentos
def saludar(titulo, nombre, *args, **kwargs):
    print(f'Hola {titulo} - {nombre}')
    print(args, kwargs)

saludar('inge', 'blonder')
