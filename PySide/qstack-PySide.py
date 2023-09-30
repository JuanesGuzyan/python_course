from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QStackedLayout, QVBoxLayout, QHBoxLayout, \
    QPushButton


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un bg
        self.setAutoFillBackground(True)
        paletacolores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletacolores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente
        self.setPalette(paletacolores)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts en PySide')
        # Layout QStackedLayout
        # Creamos los layouts
        layout_principal = QVBoxLayout()
        layout_botones = QHBoxLayout()
        self.layout_tipo_stack = QStackedLayout()
        # Agregamos los layouts hijos al layout principal
        layout_principal.addLayout(layout_botones)
        layout_principal.addLayout(self.layout_tipo_stack)
        # Creamos los botones
        boton_rojo = QPushButton('Rojo')
        # Publicar boton en el layout de botones
        layout_botones.addWidget(boton_rojo)
        # Publicamos color rojo al layout tipo stack
        self.layout_tipo_stack.addWidget(Color('red'))
        # Conectamos el evento pressed del boton respectivo
        boton_rojo.pressed.connect(lambda: self.activar_tabulador(0))

        boton_azul = QPushButton('Azul')
        layout_botones.addWidget(boton_azul)
        self.layout_tipo_stack.addWidget(Color('blue'))
        boton_azul.pressed.connect(lambda: self.activar_tabulador(1))

        boton_amarillo = QPushButton('Amarillo')
        layout_botones.addWidget(boton_amarillo)
        self.layout_tipo_stack.addWidget(Color('yellow'))
        boton_amarillo.pressed.connect(lambda: self.activar_tabulador(2))

        componente = QWidget()
        componente.setLayout(layout_principal)
        # componente_con_color_fondo = Color('red')
        # El componente se expande para cubrir el tamaño disponible
        self.setCentralWidget(componente)

    def activar_tabulador(self, indice):
        self.layout_tipo_stack.setCurrentIndex(indice)
        print(f'Indice seleccionado: {indice}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
