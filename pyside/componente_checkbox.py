from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox

class ComponenteCheckbox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente Checkbox')
        self.setFixedSize(600,400)
        self.__checkbox = QCheckBox('seleccione')
        self.__checkbox.setTristate(True)   # Activamos el tercer estado
        self.__checkbox.stateChanged.connect(self.__mostrar_estado)
        self.setCentralWidget(self.__checkbox)

    def __mostrar_estado(self, checked):
        '''
        Verifica el estado del checkbox
        Parameters
        ----------
        checked: int
            valor del checkbox
        '''
        
        #print(self.__checkbox.isChecked())
        '''
        if checked == 0:
            print('no seleccionado')
        elif checked == 1:
            print('parcialmente seleccionado')
        elif checked == 2:
            print('seleccionado')
        '''
        estado = str(self.__checkbox.checkState())

        if estado == 'CheckState.Unchecked':
            print('no seleccionado')
        elif estado == 'CheckState.PartiallyChecked':
            print('parcialmente seleccionado')
        elif estado == 'CheckState.Checked':
            print('seleccionado')

if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteCheckbox()
    ventana.show()
    app.exec()
