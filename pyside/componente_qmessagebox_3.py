from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class ComponenteQMessageBox3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.setWindowTitle('Componente QMessageBox')
        self.__boton = QPushButton('click')
        self.__boton.clicked.connect(self.__click)
        self.setCentralWidget(self.__boton)

    def __click(self, estado):
        print(f'Click: {estado}')
        self.__dialogo = QMessageBox.question(self, 'Pregunta', 'Ventana con pregunta')

        if self.__dialogo == QMessageBox.Yes:
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQMessageBox3()
    ventana.show()
    app.exec()
