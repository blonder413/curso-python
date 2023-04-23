from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox

class ComponenteQSpinBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente QSpinBox')
        self.__spin = QSpinBox()    # solo recibe valores int
        #self.__spin = QDoubleSpinBox()  # recibe valores double
        #self.__spin.setMinimum(4)
        #self.__spin.setMaximum(13)
        self.__spin.setRange(4, 13)
        self.__spin.setPrefix('B')
        self.__spin.setSuffix('.00')
        self.__spin.setSingleStep(2)    # cantidad de valores al aumentar
        
        self.__spin.valueChanged.connect(self.__cambio_valor)
        self.__spin.textChanged.connect(self.__cambio_texto)
        
        self.setCentralWidget(self.__spin)

    def __cambio_valor(self, valor):
        print(f'valor: {valor}')

    def __cambio_texto(self, texto):
        print(f'Texto: {texto}')

if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQSpinBox()
    ventana.show()
    app.exec()

