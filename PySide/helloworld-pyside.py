# Qapplication
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Clase base de Qt (PySide)
# Se encarga de procesar los eventos (event loop)
app = QApplication()
# Crear un objeto ventana
# ventana = QPushButton('Boton PySide'), cualquier componente puede ser ventana
# ventana = QWidget()
ventana = QMainWindow()
# QMainWindow trae mas interes cuando trabajamos con objetos
# Cambiar el titulo
ventana.setWindowTitle('Aplicacion Beta - PySide')
# Modificar ancho y alto de la ventana
ventana.resize(600, 400)
# Mostrar la ventana
ventana.show()
# Se ejecuta la aplicacion
sys.exit(app.exec())
