import copy

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto({self.x!r}, {self.y})"
    
    def __eq__(self, otro):
        return isinstance(otro, Punto) and self.x == otro.x and self.y == otro.y


class Rectangulo:
    def __init__(self, sup_izq, inf_der):
        self.sup_izq = sup_izq
        self.inf_der = inf_der
    
    def __repr__(self):
        return f'Rectangulo({self.sup_izq!r}, {self.inf_der!r})'


if __name__ == '__main__':
    rect_a = Rectangulo(Punto(0, 1), Punto(3, 4))
    # copia superficial
    rect_b = copy.copy(rect_a)
    print(f'rect a: {rect_a}')
    print(f'rect b: {rect_b}')
    # un cambio en un punto afecta a ambos objetos
    rect_a.inf_der.y = 6
    print(f'rect a: {rect_a}')
    print(f'rect b: {rect_b}')

    # copia profunda
    rect_c = copy.deepcopy(rect_a)
    # un cambio en un punto no afecta a ambos objetos
    rect_a.inf_der.x = 8
    print('copia profunda'.center(50, '-'))
    print(f'rect a: {rect_a}')
    print(f'rect c: {rect_c}')
