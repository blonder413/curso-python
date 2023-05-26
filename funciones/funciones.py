'''
Toda función retorna por defecto None a menos que se especifique un retorno
los parámetros son las variables que se declaran en la función
los argumentos son los valores que usamos cuando llamamos la función
principio del buen desarrollo de software DRY (Don't Repeat Yourself)
'''
def funcion_vacia():... # Podemos pasar ... para definir una función sin contenido

print(funcion_vacia())

def nada_para_hacer():  # usamos pass para definir que no vamos a poner contenido
    pass

def saludo():
    return 'hola mundo'
def saludar(nombre):
    '''
    Requiere el parámetro nombre
    '''
    return f'hola {nombre}'

print(saludar('Nemesis')) # Pasamos el argumento 'Nemesis'

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

listar_nombres('jill', 'chris')

def function(tupla):
    print(tupla)

function((1,2))

def min_max(elementos):
    '''
    aunque se puede definir que una función regrese varios valores en realidad regresa una tupla
    '''
    return min(elementos), max(elementos)

#min, max = min_max([1,2,3,4,5])
#print(min,max)

min = min_max([1,2,3,4,5])
print(type(min))
