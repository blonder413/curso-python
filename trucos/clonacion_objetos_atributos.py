import copy

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto({self.x!r}, {self.y})"
    
    def __eq__(self, otro):
        return isinstance(otro, Punto) and self.x == otro.x and self.y == otro.y


punto_a = Punto(4, 13)
# copia poco profunda
punto_b = copy.copy(punto_a)
print(f'punto a: {punto_a}')
print(f'punto b: {punto_b}')
print(f'mismo contenido: {punto_a == punto_b}')
print(f'misma referencia: {punto_a is punto_b}')
