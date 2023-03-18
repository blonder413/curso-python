try:
    numero_1 = 4
    numero_2 = '13'
    print(f'{numero_1 / numero_2}')
except ZeroDivisionError as error:
    print(error)
except TypeError as error:
    print('error')  # se recibe un string en lugar de un entero
finally:
    print('finalmente')

try:
    numero_1 = 413
    numero_2 = int(input('ingrese el número: '))
    print(f'{numero_1 / numero_2}')
except ZeroDivisionError as error:
    print(error)
except ValueError as error: # ingresamos un valor que no puede ser convertido a int
    print(error)

try:
    numero = int(input('ingrese el número: '))
    if numero < 0:
        raise TypeError('Debe ingresar un entero')
except ZeroDivisionError as error:
    print(error)
except ValueError as error: # ingresamos un valor que no puede ser convertido a int
    print(error)
except TypeError as error:
    print(error.args[0])  # se recibe el error personalizado
