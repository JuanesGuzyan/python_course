# Profundizando en el tipo str
# Docstring para documentar, se deben de autodocumentar. Mínimo necesario
import math
from mi_clase import MiClase

# Concatenacion automatica en python
# variable = 'Adios '
# mensaje = 'Hola ' 'World ' + variable
# mensaje += 'Universidad ' 'Python'
# print(mensaje)

# help(str.capitalize)
help(math.isnan)
# help(MiClase)
# print(MiClase.__doc__) unicamente doc de la clase
print(MiClase.__init__.__doc__)
print(MiClase.mi_metodo.__doc__)  # es un objeto en si mismo el metodo
print(MiClase.mi_metodo)  # referencia en memoria es un objeto
print(type(MiClase.mi_metodo))

'''
comentario
varias
lineas
'''
