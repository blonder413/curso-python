from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, QPushButton

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        self.__paleta = self.palette()
        self.__paleta.setColor(QPalette.Window, QColor(color))
        self.setPalette(self.__paleta)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.setWindowTitle('Ejemplo QStackedLayout')

        self.__layout_principal = QVBoxLayout()
        self.__layout_botones = QHBoxLayout()
        self.__layout_apilado = QStackedLayout()

        self.__layout_principal.addLayout(self.__layout_botones)
        self.__layout_principal.addLayout(self.__layout_apilado)

        self.__boton_amarillo = QPushButton('Amarillo')
        self.__boton_azul = QPushButton('Azul')
        self.__boton_rojo = QPushButton('Rojo')

        self.__layout_botones.addWidget(self.__boton_amarillo)
        self.__layout_botones.addWidget(self.__boton_azul)
        self.__layout_botones.addWidget(self.__boton_rojo)

        self.__layout_apilado.addWidget(Color('yellow'))
        self.__layout_apilado.addWidget(Color('blue'))
        self.__layout_apilado.addWidget(Color('red'))

        self.__boton_amarillo.clicked.connect(lambda: self.__mostrar_color(0))
        self.__boton_azul.clicked.connect(lambda: self.__mostrar_color(1))
        self.__boton_rojo.clicked.connect(lambda: self.__mostrar_color(2))

        self.__componente = QWidget()
        self.__componente.setLayout(self.__layout_principal)
        self.setCentralWidget(self.__componente)
    
    def __mostrar_color(self, index):
        self.__layout_apilado.setCurrentIndex(index)

app = QApplication()
ventana = Ventana()
ventana.show()
app.exec()
