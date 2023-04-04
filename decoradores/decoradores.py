'''
Un decorador es una función que recibe una función y regresa otra
se usa para extender funionalidad
Puede ejecutar funcionalidad antes o después de ejecutar la función
1. función decorador (a)
2. función a decorar (b)
3. función decorada (c)
'''

def funcion_deorador_a(funcion_a_decorar_b):
    '''
    recibe como parámetro la función a decorar (mostrar_mensaje)
    '''
    def funcion_decorada_c():
        print('antes')
        funcion_a_decorar_b()   # mostrar_mensaje
        print('después')
    
    return funcion_decorada_c


@funcion_deorador_a
def mostrar_mensaje():
    print('hola desde mostrar_mensaje')

mostrar_mensaje()