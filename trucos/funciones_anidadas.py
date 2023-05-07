def mostrar(texto):
    def minusculas(t):
        '''
        esta función solo se puede llamar desde la función mostrar
        '''
        return t.lower()
    
    return f'texto en minúsculas: {minusculas(texto)}'

print(mostrar('HOLA BLONDER'))
