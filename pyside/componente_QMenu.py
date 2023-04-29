from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QMessageBox
import os

ruta_archivo = os.path.dirname(os.path.realpath(__file__))
archivo_acerca = os.path.join(ruta_archivo, 'img/acerca.png')
archivo_nuevo = os.path.join(ruta_archivo, 'img/nuevo.png')

class ComponenteQMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente QMenu')
        self.resize(600,400)

        self.__boton_nuevo = QAction(QIcon(archivo_nuevo),'Nuevo', self)

        boton_acerca = QAction(QIcon(archivo_acerca),'&Acerca', self)
        boton_acerca.triggered.connect(self.__click_acerca)

        self.__boton_salir = QAction('&Salir', self)
        self.__boton_salir.triggered.connect(self.__salir)

        self.__menu = self.menuBar()
        self.__menu_archivo = self.__menu.addMenu('&Archivo')
        self.__menu_archivo.addAction(self.__boton_nuevo)
        
        self.__menu_archivo.addSeparator()
        
        menu_ayuda = self.__menu.addMenu('Acer&ca de')
        menu_ayuda.addAction(boton_acerca)

        self.__menu_archivo.addMenu(menu_ayuda)
        self.__menu_archivo.addAction(self.__boton_salir)

        boton_acerca.setShortcut(QKeySequence('Ctrl+A'))
        self.__boton_salir.setShortcut(Qt.CTRL | Qt.Key_X)
        
    def __click_acerca(self):
        texto = '''
        Desarrollado por Blonder413
        Todos los derechos reservados (2023)
        '''
        self.__mensaje = QMessageBox()
        self.__mensaje.setText(texto)
        self.__mensaje.setWindowTitle('Acerca de')
        self.__mensaje.exec()
        #self.__mensaje.about(self, 'Acerca de', texto)

    def __salir(self):
        exit()


if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQMenu()
    ventana.show()
    app.exec()
