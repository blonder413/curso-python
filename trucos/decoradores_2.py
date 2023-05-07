def mayusculas(funcion):
    print('antes de la llamada a la función a decorar')
    def envolvente():
        return funcion().upper()
    print('despues de la llamada a la función a decorar')
    return envolvente

@mayusculas
def minusculas():
    return 'hola'

print(minusculas())
