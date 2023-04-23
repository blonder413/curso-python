from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget

class ComponenteQListWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget')
        self.__qlist = QListWidget()
        self.__qlist.addItem('uno')
        self.__qlist.addItems(['tres','cuatro','cinco'])
        self.__qlist.currentItemChanged.connect(self.__cambio_elemento)
        self.__qlist.currentTextChanged.connect(self.__cambio_texto)
        self.setCentralWidget(self.__qlist)

    def __cambio_elemento(self, elemento):
        print(f'Elemento: {elemento.text()}')

    def __cambio_texto(self, texto):
        print(f'Texto: {texto}')

if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQListWidget()
    ventana.show()
    app.exec()
