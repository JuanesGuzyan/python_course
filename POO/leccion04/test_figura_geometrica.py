# from FiguraGeometrica import FiguraGeometrica
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

# no se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

print('Creacion objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=2, color='rojo')
# si no queremos que se modifique un valor los pasamos a solo lectura mediante la eliminacion de set
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f'su area es: {cuadrado1.calcular_area()}')
print(cuadrado1)

# MRO = method resolution order in python
# permite conocer la jerarquia de clases
# print(Cuadrado.mro())

print('Creacion objeto rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=4, alto=5, color='Azul')
rectangulo1.alto = 15
print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')
print(rectangulo1)

# Method resolution order
print(Cuadrado.mro())
