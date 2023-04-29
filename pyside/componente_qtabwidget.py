from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        self.__paleta = self.palette()
        self.__paleta.setColor(QPalette.Window, QColor(color))
        self.setPalette(self.__paleta)

class ComponenteQtabWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente QTabWidget')
        self.resize(600,400)

        self.__tab = QTabWidget()
        #self.__tab.setTabPosition(QTabWidget.East)
        self.__tab.setTabPosition(QTabWidget.North)
        self.__tab.setMovable(True)
        self.__tab.setDocumentMode(True)    # Para MacOS

        self.__tab.addTab(Color('yellow'), 'Amarillo')
        self.__tab.addTab(Color('blue'), 'Azul')
        self.__tab.addTab(Color('red'), 'Rojo')

        self.setCentralWidget(self.__tab)

if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQtabWidget()
    ventana.show()
    app.exec()
