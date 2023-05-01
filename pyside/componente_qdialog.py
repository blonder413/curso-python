from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

class ComponenteQDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.setWindowTitle('Componente QDialog')
        self.__boton = QPushButton('ver mensaje')
        self.__boton.clicked.connect(self.__click_boton)
        self.setCentralWidget(self.__boton)

    def __click_boton(self):
        print(f'Click sobre el botón')
        self.__dialogo = QDialog(self)
        self.__dialogo.setWindowTitle('Ayuda') # Crea un event loop
        self.__dialogo.exec()


if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQDialog()
    ventana.show()
    app.exec()
