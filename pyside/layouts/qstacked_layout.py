from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget

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
        self.setWindowTitle('QStackedLayout')

        self.__layout = QStackedLayout()
        self.__layout.addWidget(Color('red'))
        self.__layout.addWidget(Color('yellow'))
        self.__layout.addWidget(Color('blue'))
        self.__layout.setCurrentIndex(1)

        self.__componente = QWidget()
        self.__componente.setLayout(self.__layout)
        self.setCentralWidget(self.__componente)

app = QApplication()
ventana = Ventana()
ventana.show()
app.exec()
