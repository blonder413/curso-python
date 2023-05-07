def validar(nombre_completo):
    if len(nombre_completo) < 3:
        raise ValueError
    else:
        return 'Correcto'

nombre = 'ai'
# print(validar(nombre))

# el mismo nombre de la clase indica el problema
class NombreDemasiadoCorto(ValueError):
    pass

def validar_mejorado(nombre_completo):
    if len(nombre_completo) < 3:
        raise NombreDemasiadoCorto(nombre_completo)
    else:
        return 'Correcto'

nombre = 'ai'
print(validar_mejorado(nombre))
