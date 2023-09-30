# Las funciones en python son ciudadanas de primera clase
# First Class Citizens - en cualquier parte de nuestro codigo

# Definimos la funcion
def sumar(a, b):
    return a + b


# 1. Asignar una funcion a una variable (no se usan parentesis)
mi_funcion = sumar

# Verificar el tipo de variable
print(type(mi_funcion))
# Llamamos la funcion a traves de la variable
resultado = mi_funcion(5, 7)
print(f'Resultado: {resultado}')


# 2. Funcion como argumento
def operacion(a, b, sumar_arg):
    print(f'Resultado sumar: {sumar_arg(a, b)}')


operacion(4, 5, sumar)


# 3. Podemos retornar una funcion
def retornar_funcion():
    # Retornamos una funcion
    return sumar


mi_funcion_retornada = retornar_funcion()
print(f'Resultado funcion retornada: {mi_funcion_retornada(5, 7)}')
