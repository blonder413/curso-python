"""
assert nos permite realizar pruebaso validaciones
"""
class Persona:
    def __init__(self, edad):
        assert edad >= 0, f"La edad {edad} debe ser mayor que 0"


try:
    jill = Persona(-413)
except AssertionError as e:
    print(e)
