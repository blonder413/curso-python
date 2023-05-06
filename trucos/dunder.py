'''
dunder = double underscore
'''

class Dunder():
    def __init__(self):
        '''
        si usamos __ al principio y al final no se aplica name mangling
        esas variables no se consideran como privadas
        '''
        self.__variable_dunder__ = 4
        self.__variable_privada = 13

if __name__ == '__main__':
    d = Dunder()
    print(dir(d))
    print(d.__variable_dunder__)
    print(d._Dunder__variable_privada)
