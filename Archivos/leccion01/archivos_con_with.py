from ManejoArchivos import ManejoRecursos
# with open('prueba.txt', 'r', encoding='utf8') as archivo:
with ManejoRecursos('prueba.txt') as archivo:
    print(archivo.read())
# se conoce como context manager
