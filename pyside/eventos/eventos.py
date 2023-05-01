from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class Eventos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400,200)
        self.setWindowTitle('Eventos')
        self.__etiqueta = QLabel('click en la ventana')
        self.setCentralWidget(self.__etiqueta)

    def mouseMoveEvent(self, evento):
        '''
        Sobreescribimos el método de la clase padre
        '''
        self.__etiqueta.setText('evento mouse move event')

    def mousePressEvent(self, evento):
        self.__etiqueta.setText('evento mouse pess')

    def mouseReleaseEvent(self, evento):
        self.__etiqueta.setText('Evento mouse release')

    def mouseDoubleClickEvent(self, evento):
        self.__etiqueta.setText('Evento mouse double click')


if __name__ == '__main__':
    app = QApplication()
    ventana = Eventos()
    ventana.show()
    app.exec()
