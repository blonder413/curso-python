from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class ComponenteQMessageBox2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente QMessageBox')
        self.resize(600,400)
        self.__boton = QPushButton('click')
        self.__boton.clicked.connect(self.__click)
        self.setCentralWidget(self.__boton)

    def __click(self, estado):
        print(f'click: {estado}')
        self.__dialogo = QMessageBox(self)
        self.__dialogo.setWindowTitle('diálogo simple')
        self.__dialogo.setText('Se considera buen programador?')

        self.__dialogo.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.__dialogo.setIcon(QMessageBox.Question)

        self.__valor_retornado = self.__dialogo.exec()

        if self.__valor_retornado == QMessageBox.Yes:
            print('Mentiroso')
        else:
            print('No')


if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQMessageBox2()
    ventana.show()
    app.exec()
