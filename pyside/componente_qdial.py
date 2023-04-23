from PySide6.QtWidgets import QApplication, QMainWindow, QDial

class ComponteQDial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente QDial')
        self.__qdial = QDial()

        self.__qdial.setMinimum(4)
        self.__qdial.setMaximum(13)
        self.__qdial.setRange(4, 13)

        self.__qdial.valueChanged.connect(self.__cambio_valor)
        self.__qdial.sliderMoved.connect(self.__cambio_posicion)
        self.__qdial.sliderPressed.connect(self.__presionado)
        self.__qdial.sliderReleased.connect(self.__liberado)

        self.setCentralWidget(self.__qdial)

    def __cambio_valor(self, valor):
        print(f'valor: {valor}')

    def __cambio_posicion(self, posicion):
        print(f'posicion: {posicion}')
    
    def __presionado(self):
        print(f'presionado')
    
    def __liberado(self):
        print(f'liberado')

if __name__ == '__main__':
    app = QApplication()
    ventana = ComponteQDial()
    ventana.show()
    app.exec()
