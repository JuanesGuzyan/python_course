# Funcion closure - encapsula a otra funcion - mantiene un estado
# la funcion anidada puede acceder a las variables locales definidas
# en la funcion principal o externa
'''
# Funcion principal
def operacion(a, b):
    # definimos una funcion interna o anidada
    def sumar():
        return a + b

    # retornar la funcion
    return sumar
'''
# Funcion principal
def operacion(a, b):
    # 1. Definimos una funcion lambda interna o anidada y la retornamos
    return lambda: a + b

mi_funcion_closure = operacion(5, 2)
print(f'Resultado de la funcion closure: {mi_funcion_closure()}')

# Llamar la funcion regresada al vuelo
print(f'Resultado de la funcion closure al vuelo: {operacion(2, 3)()}')
