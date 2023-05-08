class MiClase:
    def metodo_instancia(self):
        '''
        el nombre del parámetro no debe ser self pero es lo recomendado
        puede acceder a los atributos y métodos de instancia
        '''
        return 'Método de instancia ejecutado', self
    
    @classmethod
    def metodo_de_clase(cls):
        '''
        puede acceder a los atributos y métodos de la clase
        '''
        return 'Método de clase ejecutado', cls
    
    @staticmethod
    def metodo_statico():
        '''
        No tienen acceso a la información de la clase ni de la instancia
        métodos de utileria
        '''
        return 'Método estático ejecutado'
    

if __name__ == '__main__':
    obj = MiClase()
    print(obj.metodo_instancia())
    print(MiClase.metodo_instancia(obj))

    print(obj.metodo_de_clase())
    print(MiClase.metodo_de_clase())
    
    print(obj.metodo_statico())
    print(MiClase.metodo_statico())
