from functools import partial
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton

class CalcularaPyside(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setFixedSize(235,235)
        self.__igual = False
        self.__componente_general = QWidget()
        self.setCentralWidget(self.__componente_general)
        self.__layout_principal = QVBoxLayout()
        self.__componente_general.setLayout(self.__layout_principal)
        self.__crear_area_captura()
        self.__crear_botones()
        self.__conectar_botones()

    def __crear_area_captura(self):
        self.__linea_entrada = QLineEdit()
        self.__linea_entrada.setFixedHeight(35)
        self.__linea_entrada.setAlignment(Qt.AlignRight)
        self.__linea_entrada.setReadOnly(True)
        self.__layout_principal.addWidget(self.__linea_entrada)
    
    def __crear_botones(self):
        #self.__botones = {}
        self.__layout_botones = QGridLayout()
        self.__botones = {
            '7':(0,0),
            '8':(0,1),
            '9':(0,2),
            '/':(0,3),
            '4':(1,0),
            '5':(1,1),
            '6':(1,2),
            '*':(1,3),
            '1':(2,0),
            '2':(2,1),
            '3':(2,2),
            '-':(2,3),
            '0':(3,0),
            '.':(3,1),
            'C':(3,2),
            '+':(3,3),
            '=':(3,4)
        }
        for texto_boton, posicion in self.__botones.items():
            self.__botones[texto_boton] = QPushButton(texto_boton)
            self.__botones[texto_boton].setFixedSize(40,40)
            self.__layout_botones.addWidget(self.__botones[texto_boton], posicion[0], posicion[1])
        self.__layout_principal.addLayout(self.__layout_botones)

    def __conectar_botones(self):
        for texto_boton, boton in self.__botones.items():
            if texto_boton not in {'=', 'C'}:
                boton.clicked.connect(partial(self.__construir_expresion, texto_boton))
            
        self.__botones['C'].clicked.connect(self.__limpiar_linea_entrada)
        self.__botones['='].clicked.connect(self.__calcular_resultado)
        self.__linea_entrada.returnPressed.connect(self.__calcular_resultado)

    def __construir_expresion(self, texto_boton):
        if self.__igual:
            self.__igual = False
            self.__limpiar_linea_entrada()
        
        expresion = self.__obtener_texto() + texto_boton
        self.__actualizar_texto(expresion)

    def __obtener_texto(self):
        return self.__linea_entrada.text()

    def __actualizar_texto(self, texto):
        self.__linea_entrada.setText(texto)
        self.__linea_entrada.setFocus()

    def __limpiar_linea_entrada(self):
        self.__actualizar_texto('')
    
    def __calcular_resultado(self):
        resultado = self.__evaluar_expresion(self.__obtener_texto())
        self.__actualizar_texto(resultado)
    
    def __evaluar_expresion(self, expresion):
        try:
            resultado = str(eval(expresion))
        except Exception as e:
            resultado = 'Error'
        self.__igual = True
        return resultado


if __name__ == '__main__':
    app = QApplication()
    ventana = CalcularaPyside()
    ventana.show()
    app.exec()

'''
instalar extension sourcery
'''