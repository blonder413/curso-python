def calculadora(a,b, operacion='sumar'):
    def sumar(a,b):
        return a + b

    def restar(a,b):
        return a - b

    if operacion == 'sumar':
        print(sumar(a,b))
    elif operacion == 'restar':
        print(restar(a,b))

calculadora(4, 13, 'restar')
