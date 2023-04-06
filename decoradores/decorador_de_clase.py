'''
metaprogramación
'''
import inspect


def decorador_repr(cls):
    print('Se ejecuta el decorador')
    print(f'recibimos el objeto de la clase {cls.__name__}')
    # Revisamos los atributos
    atributos = vars(cls)
    for nombre, atributo in atributos.items():
        print(nombre, atributo)
    
    # revisamos si se ha sobreesrito __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el metodo __init__')
    
    firma_init = inspect.signature(cls.__init__)
    print(f'firma de __init__: {firma_init}')
    # recuperamos los parámetros excepto el self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'parámetros init: {parametros_init}')

    # Revisamos si los parámetros tienen un método property asociado
    for parametro in parametros_init:
        es_atributo = isinstance(atributos.get(parametro), property)
        if not es_atributo:
            raise TypeError(f'no existe un método property para {parametro}')

    return cls  # retornamos cls para instanciar el objeto

@decorador_repr
class Persona:
    def __init__(self, nombre, apellido):
        print('Iniciador')
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre
        
    @property
    def apellido(self):
        return self._apellido
    
    #def __repr__(self):
    #    return f'Persona({self._nombre}, {self._apellido})'

persona1 = Persona('juan', 'pérez')
