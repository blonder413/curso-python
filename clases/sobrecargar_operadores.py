'''
Los operadores se pueden sobreescribir para que realicen lo que deseamos
+   __add__         <   __lt__
-   __sub__         <=  __le__
*   __mul__         >   __gt__
**  __pow__         >=  __ge__
/   __truediv__     ==  __eq__
//  __floordiv__    !=  __ne__
*   __mod__
'''
class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
    
    def __lt__(self, otro):
        '''
        sobrecargamos el operador <
        '''
        return self.nombre < otro.nombre
    
    def __add__(self, otro):
        '''
        Sobrecargamos el operador +
        '''
        return f'{self.nombre} y {otro.nombre}'

personas = [
    Persona('jJill', 'jvalentine@bsaa.org'),
    Persona('chris', 'creddfield@bsaa.org'),
    Persona('claire', 'credfield@terrasave.org')
]

personas.sort() # Requiere el operador < para ordenar, lo sobrecargamos para decirle que ordene por nombre
for v in personas:
    print(v.nombre)

print(personas[1] + personas[2])
