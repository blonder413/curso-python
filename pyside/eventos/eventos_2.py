from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class Eventos2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400,200)
        self.setWindowTitle('Eventos')
        self.__etiqueta = QLabel('Click en la ventana')
        self.setCentralWidget(self.__etiqueta)

    def mousePressEvent(self, evento):
        if evento.button() == Qt.LeftButton:
            self.__etiqueta.setText('mouse press click izquierdo')
        elif evento.button() == Qt.MiddleButton:
            self.__etiqueta.setText('mouse press click central')
        elif evento.button() == Qt.RightButton:
            self.__etiqueta.setText('mouse press click derecho')
        else:
            self.__etiqueta.setText('mouse press otro botón')

    def mouseReleaseEvent(self, evento):
        pass

    def mouseDoubleClickEvent(self, evento):
        pass


if __name__ == '__main__':
    app = QApplication()
    ventana = Eventos2()
    ventana.show()
    app.exec()
