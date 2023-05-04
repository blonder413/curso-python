'''
Las aserciones pueden ayudar a depurar nuestros programas de errores que no podemos recuperar
'''
def dividir(a,b):
    # assert b != 0
    assert b != 0, 'División entre cero' # el mensaje entre '' es opcional
    # si lo anterior es verdadero continúa el código
    print(f'El resultado es {a/b}')


def promedio(calificaciones):
    '''
    si la lista de calificaciones esta vacía no debería continuar el programa
    '''
    assert len(calificaciones) != 0, 'lista vacía'
    print(f'El promedio es {sum(calificaciones) / len(calificaciones)}')


def descuento(productos, descuento):
    precio_con_descuento = productos['precio'] * (1.0 - descuento)
    print(f'nuevo precio: {precio_con_descuento}')
    assert 0 <= precio_con_descuento <=productos['precio'], f'descuento inválido {precio_con_descuento}'
    print('descuento válido')


if __name__ == '__main__':
    # dividir(5, 0)
    # promedio([])
    descuento({'precio' : 413}, 1.10)
