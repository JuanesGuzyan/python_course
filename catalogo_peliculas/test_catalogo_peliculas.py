from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalagoPeliculas

opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar pelicula')
        print('2. Listar Peliculas')
        print('3. Eliminar catalogo peliculas')
        print('4. Salir')
        opcion = int(input('Escribe tu opcion (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            CatalagoPeliculas.agregar_pelicula(pelicula)
        elif opcion == 2:
            CatalagoPeliculas.listar_peliculas()
        elif opcion == 3:
            CatalagoPeliculas.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
else:
    print('Salimos del programa')
