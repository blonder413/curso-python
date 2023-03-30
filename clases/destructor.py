'''
El destructor se usa cuando eliminamos explícitamente el objeto
'''
class Destructor:
    def __del__(self):
        print('Se ha destruido el objeto')

objeto = Destructor()
del objeto  # Destruimos el objeto
# No es necesario eliminar los objetos ya que Python se encarga de hacerlo de forma automática