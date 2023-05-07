'''
es buena idea crear una clase base y heredar otras clases
'''
class ClaseExcepcionBase(TypeError):
    pass


class NombreDemasiadoCorto(ClaseExcepcionBase):
    pass


def validar_mejorado(nombre_completo):
    if len(nombre_completo) < 3:
        raise NombreDemasiadoCorto(nombre_completo)
    else:
        return 'Correcto'

nombre = 'ai'
try:
    print(validar_mejorado(nombre))
except ClaseExcepcionBase as e:
    print(f'Tipo: {type(e).__name__}, línea: {e.__traceback__.tb_lineno}, archivo: {__file__}: {e}')
