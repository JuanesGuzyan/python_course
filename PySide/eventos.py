from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eventos')
        self.etiqueta = QLabel('Da clic en esta ventana')
        self.setCentralWidget(self.etiqueta)

    def mousePressEvent(self, event):
        # Preguntamos por el boton del mouse que lanzo el evento
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('mousePressEvent boton izquierdo')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('mousePressEvent boton central')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('mousePressEvent boton derecho')

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('mouseReleaseEvent boton izquierdo')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('mouseReleaseEvent boton central')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('mouseReleaseEvent boton derecho')

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('mouseDoubleClickEvent boton izquierdo')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('mouseDoubleClickEvent boton central')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('mouseDoubleClickEvent boton derecho')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
