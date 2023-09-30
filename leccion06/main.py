# tenemos que definir primero la función para mandarla a llamar
def mi_funcion(nombre, apellido):
    print('Saludos desde la función')
    print(f'Nombre: {nombre}, Apellido: {apellido}')


mi_funcion('Pedro', 'Perez')
mi_funcion('Karla', 'Lara')


# parametros variables declarados en la funcion y argumentos valor que enviamos a la funcion
# datos en python son dinámicos
# def sumar (a:int = 0, b:int = 0) -> int: es redundante en python
def sumar(a=0, b=0):
    return a + b


resultado = sumar()
print(f'Resultado de la suma: {resultado} ')

print(f'resultado sumar: {sumar(5, 3)}')


# lo vamos a usar como si fuera una tupla(no se puede modificar)
# en la documentación de python vamos a encontrar def listarNombres(*args):
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Juan', 'Karla', 'María', 'Ernesto')
listarNombres('Laura', 'Carlos')
