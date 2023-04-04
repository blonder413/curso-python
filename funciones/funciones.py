'''
los parámetros son las variables que se declaran en la función
los argumentos son los valores que usamos cuando llamamos la función
'''
def funcion_vacia():... # Podemos pasar ... para definir una función sin contenido

def nada_para_hacer():  # usamos pass para definir que no vamos a poner contenido
    pass

def saludo():
    return 'hola mundo'
def saludar(nombre):
    '''
    Requiere el parámetro nombre
    '''
    return f'hola {nombre}'

print(saludar('Jonathan')) # Pasamos el argumento 'Jonathan'

def despedir(mensaje = 'chao'):
    return mensaje

def sumar(num1: int = 0, num2: int = 0) -> int:
    '''
    Aunque podemos definir el tipo de dato de los parámetros y de retorno, estos tipos no son estrictos, 
    solo sirven de ayuda visual
    '''
    return num1 + num2

def listar_nombres(*nombres):   # Este se trata como una tupla
    print(type(nombres))
    for value in nombres:
        print(value)

listar_nombres('jonathan', 'bridyith')

def min_max(elementos):
    '''
    aunque se puede definir que una función regrese varios valores en realidad regresa una tupla
    '''
    return min(elementos), max(elementos)

#min, max = min_max([1,2,3,4,5])
#print(min,max)

min = min_max([1,2,3,4,5])
print(type(min))
