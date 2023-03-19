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

personas = [
    Persona('jonathan', 'blonder413@gmail.com'),
    Persona('bridyith', 'bridyith@hotmail.com'),
    Persona('anyi', 'acmendezmelo@gmail.com')
]

personas.sort()
for v in personas:
    print(v.nombre)
