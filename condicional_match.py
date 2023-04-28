variable = input("ingrese su nombre: ")

match variable:
    case 'pepe':
        print("hola pepe")
    case 'blonder' | 'blonder413':
        print('hola blonder')
    case _:
        print('no reconocido')
