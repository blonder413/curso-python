from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

class ComponenteCombobox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente Combobox')
        #self.setFixedSize(800,600)
        self.combo = QComboBox()
        self.combo.addItem('uno')
        self.combo.addItems(['dos','tres'])
        self.combo.addItems(('cuatro', 'cinco'))
        self.combo.currentIndexChanged.connect(self.__cambio_indice)
        self.combo.currentTextChanged.connect(self.__cambio_texto)
        self.setCentralWidget(self.combo)

    def __cambio_indice(self, indice):
        print(f'índice seleccionado: {indice}')
        print(f'valor: {self.combo.itemText(indice)}')

    def __cambio_texto(self, texto):
        print(f'texto seleccionado: {texto}')

if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteCombobox()
    ventana.show()
    app.exec()
