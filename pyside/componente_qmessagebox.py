from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class ComponenteQMessageBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.setWindowTitle('Ejemplo')
        self.__boton = QPushButton('Mostrar diálogo')
        self.__boton.clicked.connect(self.__click)
        self.setCentralWidget(self.__boton)
    
    def __click(self, estado):
        print(f'click sobre el botón: {estado}')
        self.__dialogo = QMessageBox(self)
        self.__dialogo.setWindowTitle('Diálogo simple')
        self.__dialogo.setText('ventana simple')
        self.__valor_retornado = self.__dialogo.exec()

        if self.__valor_retornado == QMessageBox.Ok:
            print('ok')
        else:
            print('no ok')

if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQMessageBox()
    ventana.show()
    app.exec()
