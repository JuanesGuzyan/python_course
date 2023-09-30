import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.setFixedSize(400, 200)
        # Definimos los elementos. Etiqueta y linea de edicion
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        # Conectar el widget de entrada_texto con la etiqueta
        # La señal es textChanged, el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # Publicamos los componentes usando un layout
        layout = QVBoxLayout()
        layout.addWidget(self.entrada_texto)
        layout.addWidget(self.etiqueta)
        # Crear un contenedor
        contenedor = QWidget()
        contenedor.setLayout(layout)
        # Publicamos el contenedor, que incluye los demas elementos
        self.setCentralWidget(contenedor)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
