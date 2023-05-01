from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class ComponenteQMessageBox4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,400)
        self.setWindowTitle('QMessageBox')
        self.__boton = QPushButton('click')
        self.__boton.clicked.connect(self.__click)
        self.setCentralWidget(self.__boton)
    
    def __click(self, estado):
        self.__dialogo = QMessageBox.critical(
            self, 
            'Crítico', 
            'Danger', 
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore, defaultButton=QMessageBox.Discard
            )
        
        if self.__dialogo == QMessageBox.Discard:
            print('discard')
        elif self.__dialogo == QMessageBox.NoToAll:
            print('not to all')
        else:
            print('ignore')

if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQMessageBox4()
    ventana.show()
    app.exec()
