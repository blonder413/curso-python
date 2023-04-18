import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes con PySide')
        self.setFixedSize(QSize(800,600))
        self.__agregar_componentes()
    
    def __agregar_componentes(self):
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        accion_nuevo = QAction('Nuevo', self)
        # se debe agregar información por defecto a la barra de estado
        accion_nuevo.setStatusTip('Nuevo Archivo')
        menu_archivo.addAction(accion_nuevo)
        self.statusBar().showMessage('')

if __name__ == '__main__':
    app = QApplication()
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
