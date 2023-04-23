from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

class ComponenteCombobox2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Combobox')
        self.__combo = QComboBox()
        self.__combo.addItems(['uno', 'dos', 'tres', 'cuatro', 'cinco'])
        self.setCentralWidget(self.__combo)
        self.__combo.setEditable(True)
        # Especificar política de inserción
        self.__combo.setInsertPolicy(QComboBox.NoInsert)
        self.__combo.setInsertPolicy(QComboBox.InsertAtTop)
        self.__combo.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.__combo.setInsertPolicy(QComboBox.InsertAtBottom)
        self.__combo.setInsertPolicy(QComboBox.InsertBeforeCurrent)
        self.__combo.setInsertPolicy(QComboBox.InsertAfterCurrent)
        self.__combo.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.__combo.setMaxCount(6)

app = QApplication()
ventana = ComponenteCombobox2()
ventana.show()
app.exec()
