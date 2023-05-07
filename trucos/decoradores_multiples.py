def negritas(funcion):
    def funcion_envolvente():
        return '<strong>' + funcion() + '</strong>'
    return funcion_envolvente

def cursivas(funcion):
    def funcion_envolvente():
        return '<i>' + funcion() + '</i>'
    return funcion_envolvente

@negritas
@cursivas
def saludar_html():
    '''
    los decoradores se ejecutan from bottom to top (de abajo hacia arriba)
    Returns
    -------
        str
            texto de saludo
    '''
    return 'hello world'

print(saludar_html())
