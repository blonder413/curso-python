n1 = 4;
n2 = "13"

# if type(n2) == int: # No se recomienda usar type para validar tipos de datos
if isinstance(n1, int) and isinstance(n2, int):
    print(n1 + n2)
else:
    print("deben ser enteros")


try:
    numero_1 = 4
    numero_2 = 0
    print(f'{numero_1 / numero_2}')
except ZeroDivisionError as error:
    print(type(error).__name__)
except TypeError as error:
    print('error')  # se recibe un string en lugar de un entero
except Exception as error:
    print('error')  # Esta es una excepción general, debe ir al final o no tomará en cuenta las demás
finally:
    print('Se ejecuta después de todo, haya o no haya excepción')

try:
    numero_1 = 413
    numero_2 = int(input('ingrese el número: '))
    print(f'{numero_1 / numero_2}')
except ZeroDivisionError as error:
    print(error)
except ValueError as error: # ingresamos un valor que no puede ser convertido a int
    print(error)
else:
    print('se ejecuta si no ocurrió ninguna excepción')

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
