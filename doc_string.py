class DocString:
    '''
    Este es un ejemplo de la documentaión de esta clase
    '''

    def __init__(self):
        '''
        Método de inicio de la clase
        '''
    def mi_metodo(self, param1, param2):
        '''
        Esta es la documentación del método
        No recomendado
        :param param1: str
        :param param2: str
        :return: str
        '''


    def suma(self, num1, num2):
        '''
        Este método realiza la suma de 2 valores
        Parameters
        ----------
        num1 : int
            Valor 1
        num2 : int
            Valor 2
        Returns
        -------
        int
            Resultado de la suma
        '''

# help(DocString)
# print(DocString.__doc__)
help(DocString.mi_metodo)
# help(DocString.suma)
