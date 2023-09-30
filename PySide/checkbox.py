import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes - PySide')
        # Crear checkbox
        checkbox = QCheckBox('Este es un checkbox')
        # Activamos el 3er estado
        checkbox.setTristate(True)
        # Conectar la señal de cambio de componente
        checkbox.stateChanged.connect(self.mostrar_estado)
        self.setCentralWidget(checkbox)

    def mostrar_estado(self, estado):
        print('Estado checkbox:', estado)
        # Trabajamos con las constantes
        if estado == Qt.Checked:
            print('Checkbox encendido')
        elif estado == Qt.PartiallyChecked:
            print('Checkbox sin estado o parcialmente checado')
        elif estado == Qt.Unchecked:
            print('Checkbox apagado')
        else:
            print('Checkbox invalido')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())
