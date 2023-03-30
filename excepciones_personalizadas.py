class ExcepcionesPersonalizadasException(Exception):
    def __init__(self, mensaje = ''):
        self.message = 'BlonderException ' + mensaje

try:
    if 0 == 0:
        raise ExcepcionesPersonalizadasException('bruto')
except ExcepcionesPersonalizadasException as e:
    print(e.message)
