from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit

class ComponenteQLineEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente QLineEdit')
        self.setStyleSheet('background-color: #FFF; color: #000')
        self.__qline = QLineEdit()
        #self.__qline.setMaxLength(8)
        self.__qline.setPlaceholderText('Celular (000-000-0000)...')
        #self.__qline.setReadOnly(True)
        self.__qline.setInputMask('000-000-0000')
        self.__qline.returnPressed.connect(self.__presionar_enter)
        self.__qline.selectionChanged.connect(self.__cambiar_seleccion)
        self.__qline.textChanged.connect(self.__cambiar_texto)
        self.setCentralWidget(self.__qline)

    def __presionar_enter(self):
        print('Se presionó el enter')
        self.centralWidget().setText('Juan Perez')

    def __cambiar_seleccion(self):
        print(self.centralWidget().selectedText())

    def __cambiar_texto(self, texto):
        print(f' Nuevo texto: {texto}')

if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQLineEdit()
    ventana.show()
    app.exec()
