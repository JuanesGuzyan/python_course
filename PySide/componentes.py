import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes - PySide')
        self.setFixedSize(500, 600)
        # Creamos un componente de tipo etiqueta (Label)
        etiqueta = QLabel('Hola')
        etiqueta.setPixmap(QPixmap('sitemap.png'))
        # Ajustar la imagen al tamaño de la ventana
        etiqueta.setScaledContents(True)
        # Modificamos el valor inicial
        # etiqueta.setText('Saludos')
        # Modificamos la fuente
        # fuente = etiqueta.font()
        # fuente.setPointSize(25)
        # etiqueta.setFont(fuente)
        # Modificar la alineacion de la etiqueta
        # etiqueta.setAlignment(Qt.AlignCenter)
        # etiqueta.setAlignment(Qt.AlignHCenter | Qt.ALignVCenter)
        # Publicamos este componente
        self.setCentralWidget(etiqueta)


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())
