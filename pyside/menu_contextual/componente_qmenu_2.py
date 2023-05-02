from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu

class ComponenteQMenu2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.setWindowTitle('Menú contextual')
        
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.__menu_contextual)
        
        self.show()

    def __menu_contextual(self, posicion):
        self.__menu = QMenu(self)
        self.__salir = QAction('salir', self)
        self.__menu.addAction(self.__salir)
        self.__menu.exec(self.mapToGlobal(posicion))

app = QApplication()
ventana = ComponenteQMenu2()
#ventana.show()
app.exec()
