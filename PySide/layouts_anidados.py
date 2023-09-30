from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QHBoxLayout, QVBoxLayout


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
        # Anidar layouts (uno dentro de otro)
        # Se crea un layout horizontal y despues uno vertical
        layout_horizontal = QHBoxLayout()
        layout_horizontal.setContentsMargins(10, 10, 10, 10)
        layout_vertical = QVBoxLayout()
        # Agregamos espacio en el layout vertical
        layout_vertical.setContentsMargins(5, 10, 5, 10)
        # Agregamos espacio dentro de cada elemento vertical
        layout_horizontal.setSpacing(25)
        layout_vertical.setSpacing(20)
        # Agregamos algunos widgets al vertical
        # Agregamos un nuevo componente de color
        layout_vertical.addWidget(Color('red'))
        layout_vertical.addWidget(Color('green'))
        layout_vertical.addWidget(Color('blue'))
        # Agregamos el layout_vertical dentro del layout horizontal
        # Es decir, se agrega de manera anidada, un layout dentro de otro
        layout_horizontal.addLayout(layout_vertical)
        # Agregamos mas elementos al horizontal
        layout_horizontal.addWidget(Color('yellow'))
        layout_horizontal.addWidget(Color('purple'))
        # Crear componente generico para publicar un layout
        componente = QWidget()
        componente.setLayout(layout_horizontal)
        # componente_con_color_fondo = Color('red')
        # El componente se expande para cubrir el tamaño disponible
        self.setCentralWidget(componente)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
