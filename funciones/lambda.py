'''
son funiones pequeñas, de una línea de código, son anónimas
no se usan paréntesis para los parámetros
no usa return pero sí debe devolver algo
'''
funcion = lambda : 'hola mundo'
funcion = lambda a,b: a + b
funcion = lambda a=2,b=3: a + b
print(funcion(4,13))

funcion = lambda *args, **kwargs: len(args) + len(kwargs)
print(funcion(1,2,3, a=5,b=3))
