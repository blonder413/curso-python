from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QCheckBox
import os

ruta_archivo = os.path.dirname(os.path.realpath(__file__))
archivo_nuevo = os.path.join(ruta_archivo, 'img/nuevo.png')
archivo_guardar = os.path.join(ruta_archivo, 'img/guardar.png')

class BarraHerramientas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.setWindowTitle('Ejemplo barra de herramientas')
        self.__etiqueta = QLabel('hola')
        self.__etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.__etiqueta)

        self.__barra = QToolBar('barra de herramientas')
        self.__barra.setIconSize(QSize(16,16))
        # self.__barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)   # se acopla al Sistema Operativo
        self.__barra.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.__barra.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.__barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.__barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(self.__barra)

        self.__boton_nuevo = QAction(QIcon(archivo_nuevo),'Nuevo', self)
        self.__boton_nuevo.triggered.connect(self.__click_boton_nuevo)
        #self.__boton_nuevo.setCheckable(True)
        
        self.__boton_guardar = QAction(QIcon(archivo_guardar), 'Guardar', self)
        self.__boton_guardar.triggered.connect(self.__click_boton_guardar)

        self.__barra.addAction(self.__boton_nuevo)
        self.__barra.addAction(self.__boton_guardar)

        self.setStatusBar(QStatusBar(self))
        self.__boton_nuevo.setStatusTip('Nuevo...')
        self.__boton_guardar.setStatusTip('Guardar...')

        self.__barra.addSeparator()

        self.__checkbox = QCheckBox()
        self.__barra.addWidget(self.__checkbox) # No se recomienda usar widgets sino qactions
    
    def __click_boton_nuevo(self, estado):
        print(f'Nuevo')
    
    def __click_boton_guardar(self):
        print('Guardando')


if __name__ == '__main__':
    app = QApplication()
    ventana = BarraHerramientas()
    ventana.show()
    app.exec()
