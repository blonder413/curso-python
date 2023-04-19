import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Slots')
        boton = QPushButton('click')
        boton.setCheckable(True)
        boton.clicked.connect(self.__evento_check)
        boton.clicked.connect(self.__evento_click)
        self.setCentralWidget(boton)

    def __evento_check(self, check):
        '''
        Verifica si el botón se quedó presionado o se soltó
        Parameters
        ----------
        check : bool
            True si está presionado
        '''
        self.boton_presionado = check
        if self.boton_presionado:
            print('presionado')
        else:
            print('soltado')

    def __evento_click(self):
        print('hizo click')
        if self.boton_presionado:
            print('presionado desde click')
        else:
            print('soltado desde click')

app = QApplication()
ventana = Ventana()
ventana.show()
sys.exit(app.exec())
