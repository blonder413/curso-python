from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        self.__paleta = self.palette()
        self.__paleta.setColor(QPalette.Window, QColor(color))
        self.setPalette(self.__paleta)

class GridLayout(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Grid Layout')
        self.resize(800,600)

        self.__layout = QGridLayout()
        self.__layout.addWidget(Color('red'), 0, 0)
        self.__layout.addWidget(Color('blue'), 0, 2)
        self.__layout.addWidget(Color('green'), 1, 1)
        self.__layout.addWidget(Color('yellow'), 2, 0)
        self.__layout.addWidget(Color('purple'), 2, 2)

        self.__componente = QWidget()
        self.__componente.setLayout(self.__layout)
        self.setCentralWidget(self.__componente)

if __name__ == '__main__':
    app = QApplication()
    ventana = GridLayout()
    ventana.show()
    app.exec()
