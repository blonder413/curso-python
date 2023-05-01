from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel

class VentanaDialog(QDialog):
    def __init__(self, padre=None):
        super().__init__(padre)
        self.setWindowTitle('Ventana de diálogo')
        self.__botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.__botones_dialogo = QDialogButtonBox(self.__botones)
        self.__botones_dialogo.accepted.connect(self.accept)
        self.__botones_dialogo.rejected.connect(self.reject)
        self.__mensaje = QLabel('click en un botón')
        self.__layout = QVBoxLayout()
        self.__layout.addWidget(self.__mensaje)
        self.__layout.addWidget(self.__botones_dialogo)
        self.setLayout(self.__layout)


class ComponenteQDialog2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.setWindowTitle('Ejemplo QDialog')
        self.__boton = QPushButton('Mostrar diálogo')
        self.__boton.clicked.connect(self.__click)
        self.setCentralWidget(self.__boton)

    def __click(self):
        print('click')
        self.__dialogo = VentanaDialog(self)
        self.__valor_retornado = self.__dialogo.exec()
        print(f'Valor retornado: {self.__valor_retornado}')

        if self.__valor_retornado:
            print('Se presionó OK')
        else:
            print('Se presionó Cancel')

if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQDialog2()
    ventana.show()
    app.exec()
