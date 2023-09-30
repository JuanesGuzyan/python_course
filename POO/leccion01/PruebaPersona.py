from Persona import Persona
# si queremos importar todas las clases utilizamos solamente import *
print('Creacion objetos'.center(50, '-'))
if __name__ == '__main__':
    persona1 = Persona('Karla', 'Gomez', 30)
    persona1.mostrar_detalle()

    print(__name__)

print('Eliminacion de objetos'.center(50, '-'))
del persona1
# recolector de basura; todos los objetos que no apunten a una variable van a ser eliminados automáticamente
# clase padre se extiende a clase hija
# herencia multiple en python
