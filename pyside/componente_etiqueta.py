from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication

class ComponenteEtiqueta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente etiqueta')
        self.setFixedSize(600,400)
        etiqueta = QLabel('Hola Blonder')
        etiqueta.setText('Chao Blonder')
        fuente = etiqueta.font()
        fuente.setPointSize(25)
        etiqueta.setFont(fuente)
        # etiqueta.setAlignment(Qt.AlignCenter)
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # con | aplicamos varias alineaciones
        self.setCentralWidget(etiqueta)

if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteEtiqueta()
    ventana.show()
    app.exec()
