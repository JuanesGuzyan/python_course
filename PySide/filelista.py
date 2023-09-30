import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes - PySide')
        # Creamos un nuevo combo box (drop down list)
        combobox = QComboBox()
        # Agregamos elementos
        combobox.addItem('Uno')
        combobox.addItems(['Dos', 'Tres'])
        # Monitoreamos el cambio de elemento seleccionado, tanto de indice como de texto
        combobox.currentIndexChanged.connect(self.cambio_indice)
        combobox.currentTextChanged.connect(self.cambio_texto)
        # Hacemos editable el combobox
        combobox.setEditable(True)
        # Politica de insercion
        # combobox.setInsertPolicy(QComboBox.NoInsert)
        # Agregar al inicio del combobox
        # combobox.setInsertPolicy(QComboBox.InsertAtTop)
        # Modificar el elemento actual
        # combobox.setInsertPolicy(QComboBox.InsertAtCurrent)
        # Insert al final
        # combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        # Insertar antes del elemento actual
        # combobox.setInsertPolicy(QComboBox.InsertBeforeCurrent)
        # Insertar despues del elemento actual
        # combobox.setInsertPolicy(QComboBox.InsertAfterCurrent)
        # Insertar alfabeticamente
        combobox.setInsertPolicy(QComboBox.InsertAlphabetically)
        # Limitar cantidad de elementos
        combobox.setMaxCount(6)
        self.setCentralWidget(combobox)

    def cambio_indice(self, nuevo_indice):
        print(f'Nuevo indice seleccionado: {nuevo_indice}')

    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto seleccionado: {nuevo_texto}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())
