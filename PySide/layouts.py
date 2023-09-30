from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout


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
        # Layout vertical
        layout = QVBoxLayout()
        # Agregamos un nuevo componente de color
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        # Crear componente generico para publicar un layout
        componente = QWidget()
        componente.setLayout(layout)
        # componente_con_color_fondo = Color('red')
        # El componente se expande para cubrir el tamaño disponible
        self.setCentralWidget(componente)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
