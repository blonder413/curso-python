from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel

class VentanaNueva(QWidget):
    '''
    Podemos usar otro tipo de clase, incluyendo QMainWindow
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nueva ventana')
        self.__layout = QVBoxLayout()
        self.__label = QLabel(f'Nueva ventana: {id(self)}')
        self.__layout.addWidget(self.__label)
        self.setLayout(self.__layout)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__nueva_ventana = None
        self.resize(200,100)
        self.setWindowTitle('Ventanas')
        self.__boton_abrir = QPushButton('&Abrir')
        self.__boton_abrir.clicked.connect(self.__abrir)
        self.__boton_cerrar = QPushButton('&Cerrar')
        self.__boton_cerrar.clicked.connect(self.__cerrar)
        self.__layout = QVBoxLayout()
        self.__layout.addWidget(self.__boton_abrir)
        self.__layout.addWidget(self.__boton_cerrar)
        self.__componente = QWidget()
        self.__componente.setLayout(self.__layout)
        self.setCentralWidget(self.__componente)

    def __abrir(self, estado):
        if self.__nueva_ventana is None:
            self.__nueva_ventana = VentanaNueva()
        self.__nueva_ventana.show()
    
    def __cerrar(self, estado):
        if self.__nueva_ventana:
            self.__nueva_ventana.close()
            self.__nueva_ventana = None


if __name__ == '__main__':
    app = QApplication()
    ventana = Ventana()
    ventana.show()
    app.exec()
