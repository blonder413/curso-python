"""
En este módulo explicamos cómo usar las clases
"""
class Ejemplo:
    """
    Esta es una clase de ejemplo
    """

    def __init__(self):
        self.nombre = 'Jonathan'

    @property
    def PI(self):
        '''
        aquí definimos la constante
        '''
        return 3.141592
    
    def get_nombre(self):
        """
        Regresamos el valor para el atributo nombre
        Returns
        -------
        str
            Valor del atributo nombre
        """
        return self.nombre
    
    def set_nombre(self, nombre):
        """
        Establecemos un valor para el atributo nombre
        Parameters
        ----------
        nombre : str
            Nombre a definir
        """
        self.nombre = nombre

ejemplo = Ejemplo()  # instanciamos

print(ejemplo.PI)  # accedemos a la constante PI
print(isinstance(ejemplo, Ejemplo))   # Saber si es instancia de una clase
ejemplo.set_nombre('blonder')
print(ejemplo.get_nombre())

ejemplo.PI = 10  # intentamos alterar la constante
