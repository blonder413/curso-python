from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        self.__paleta = self.palette()
        self.__paleta.setColor(QPalette.Window, QColor(color))
        self.setPalette(self.__paleta)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts anidads')
        self.resize(800,600)

        self.__layout_horizontal = QHBoxLayout()
        self.__layout_vertical = QVBoxLayout()

        self.__layout_horizontal.setContentsMargins(10, 10, 10, 10)
        self.__layout_vertical.setContentsMargins(5, 10, 5, 10)
        self.__layout_vertical.setSpacing(20)

        self.__layout_vertical.addWidget(Color('yellow'))
        self.__layout_vertical.addWidget(Color('blue'))
        self.__layout_vertical.addWidget(Color('red'))

        self.__layout_horizontal.addWidget(Color('black'))
        self.__layout_horizontal.addWidget(Color('white'))
        self.__layout_horizontal.addLayout(self.__layout_vertical)

        self.__componente = QWidget()
        self.__componente.setLayout(self.__layout_horizontal)
        self.setCentralWidget(self.__componente)

if __name__ == '__main__':
    app = QApplication()
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
