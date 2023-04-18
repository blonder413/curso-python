from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Slots')
        boton = QPushButton('Click')
        # permite que se quede como presionado
        boton.setCheckable(True)    # por defecto es False
        boton.clicked.connect(self.__evento_check)
        boton.clicked.connect(self.__evento_click)
        self.setCentralWidget(boton)
    
    def __evento_click(self):
        print('hola blonder')
    
    def __evento_check(self, check):
        '''
        Verifica si el botón está presionado
        Parameters
        ----------
        check : bool
            True si se ha presionado
        '''
        if check:
            print('está presionado')
        else:
            print('no está presionado')

if __name__ == '__main__':
    app = QApplication()
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
