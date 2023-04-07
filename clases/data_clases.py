'''
Es conveniente cuando las clases van a ser pequeñas, sin tantas validaciones
'''

from dataclasses import dataclass
from typing import ClassVar

#@dataclass(eq=False)   # podemos evitar que dos objetos sean iguales
@dataclass(frozen=True) # convertimos la clase en objetos inmutables
#@dataclass
class Persona:
    nombre: str # Al usar datalass se debe indicar el tipo de dato
    apellido: str
    contador: ClassVar[int] = 0   # Variable de clase

    def __post_init__(self):    # se ejecuta después de __init__
        if not self.nombre:
            raise ValueError(f'nombre vacío')

persona = Persona('juan', 'perez')
print(persona)  # ya contamos con el método __repr__
print(Persona.contador)
print(f'variables de instancia: {persona.__dict__}')

#persona_vacia = Persona('', '')
#print(persona_vacia)

# Revisar igualdad entre objetos
persona2 = Persona('juan', 'perez')
print(f'Iguales? {persona == persona2 }')

colecion = {persona, persona2}
print(colecion)
