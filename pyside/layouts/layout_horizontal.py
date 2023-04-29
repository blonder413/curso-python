from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        self.__paleta = self.palette()
        self.__paleta.setColor(QPalette.Window, QColor(color))
        self.setPalette(self.__paleta)

class VentanaPrincipial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layout Horizontal')
        self.__layout = QHBoxLayout()
        self.__layout.addWidget(Color('yellow'))
        self.__layout.addWidget(Color('blue'))
        self.__layout.addWidget(Color('red'))
        self.__componente = QWidget()
        self.__componente.setLayout(self.__layout)
        self.setCentralWidget(self.__componente)

if __name__ == '__main__':
    app = QApplication()
    ventana = VentanaPrincipial()
    ventana.show()
    app.exec()
