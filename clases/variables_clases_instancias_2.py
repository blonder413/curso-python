class ContadorObjetosErronea:
    instancias = 0

    def __init__(self):
        # error
        self.instancias += 1


class ContadorObjetos:
    instancias = 0

    def __init__(self):
        # error
        self.__class__.instancias += 1


if __name__ == '__main__':
    print('Erroneas'.center(50, '-'))
    print(ContadorObjetosErronea.instancias)
    print(ContadorObjetosErronea().instancias)
    print(ContadorObjetosErronea().instancias)
    print(ContadorObjetosErronea.instancias)
    print('Correctas'.center(50, '-'))
    print(ContadorObjetos.instancias)   # 0
    print(ContadorObjetos().instancias) # 1
    print(ContadorObjetos().instancias) # 2
    print(ContadorObjetos.instancias)   # 2
