"""
Crear una función para sumar los valores recibidos de tipo numerico, utilizando argumentos
variables *args como parámetro de la función y regresar como resultado
la suma de todos los valores pasados como argumentos
"""


# definir función de sumar valores
def sumar_valores(*args):
    resultado = 0
    # iteramos cada elemento de argumentos variables
    for valor in args:
        # resultado = resultado + valor
        resultado += valor
    return resultado


# llamada a la función
print(sumar_valores(3, 5, 9))

"""
Crear una función para multiplicar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la multiplicación de todos los valores pasados
como argumentos
"""


def multiplicar_valores(*args):
    total = 1
    for valor in args:
        total *= valor
    return total

# llamamos la funcion
print(multiplicar_valores(4, 6, 2))
