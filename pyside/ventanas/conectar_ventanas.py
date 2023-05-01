from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

class VentanaNueva(QWidget):
    '''
    Podemos usar otro tipo de clase, incluyendo QMainWindow
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nueva ventana')
        self.__layout = QVBoxLayout()
        self.label = QLabel(f'Nueva ventana: {id(self)}')
        self.__layout.addWidget(self.label)
        self.setLayout(self.__layout)

class ConectarVentanas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__nueva_ventana = VentanaNueva()
        self.resize(200,100)
        self.setWindowTitle('Ventanas')
        self.__boton_mostrar = QPushButton('&Mostrar/Ocultar')
        self.__boton_mostrar.clicked.connect(self.__mostrar)
        self.__entrada_texto = QLineEdit()
        self.__entrada_texto.textChanged.connect(self.__nueva_ventana.label.setText)
        self.__layout = QVBoxLayout()
        self.__layout.addWidget(self.__boton_mostrar)
        self.__layout.addWidget(self.__entrada_texto)
        self.__componente = QWidget()
        self.__componente.setLayout(self.__layout)
        self.setCentralWidget(self.__componente)

    def __mostrar(self, estado):
        if self.__nueva_ventana.isVisible():
            self.__nueva_ventana.hide()
        else:
            self.__nueva_ventana.show()

if __name__ == '__main__':
    app = QApplication()
    ventana = ConectarVentanas()
    ventana.show()
    app.exec()
