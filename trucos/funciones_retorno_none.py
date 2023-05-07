def funcion(valor):
    if valor:
        return valor
    else:
        return None

def funcion2(valor):
    '''
    si no se especifica un retorno, la función retorna None
    '''
    if valor:
        return valor

def funcion3(valor):
    print(valor)

if __name__ == '__main__':
    print(funcion(False))
    print(funcion2(0))
    print(f'funcion 3: {funcion3(0)}')
