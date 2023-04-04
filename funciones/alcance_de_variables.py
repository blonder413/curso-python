var_global = 'jonathan'

def imprimir():
    # si vamos a modificar el valor debemos indicar que es global, para lectura no
    global var_global
    print(f'Variable global: {var_global}')

    var_local = 'variable local'
    print(f'Variable local: {var_local}')

    # Si vamos a modificar la variable global debemos llamarla usando la palabra global
    var_global = 'nuevo valor'
    print(var_global)

imprimir()
