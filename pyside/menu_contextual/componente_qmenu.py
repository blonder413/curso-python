from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu
import os

class ComponenteQMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.setWindowTitle('Menú contextual')
        
    def contextMenuEvent(self, evento):
        '''
        Sobreescribimos el método
        '''
        self.__salir = QAction('salir', self)
        self.__salir.triggered.connect(self.__click_salir)
        self.__menu = QMenu(self)
        self.__menu.addAction(QAction('nuevo', self))
        self.__menu.addAction(QAction('guardar', self))
        self.__menu.addAction(self.__salir)
        self.__menu.exec(evento.globalPos())    # Posición el cusor
    
    def __click_salir(self):
        exit()


if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQMenu()
    ventana.show()
    app.exec()
