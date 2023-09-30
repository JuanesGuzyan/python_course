# bool contiene los valores de True y False
# Tipos Numericos, False para 0, True demas valores
# valor = 0
# resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
# valor = 15
# resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

# Tipo str, False para '', True demás valores

# valor = ''
# resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
# valor = 'hola'
# resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

# Tipo colecciones, False para colecciones vacias, True para todas las demas conexiones
# Lista
# valor = []
# resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
# valor = [2, 3, 5]
# resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
# Tupla
# valor = ()
# resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
# valor = (2, 3, 4)
# resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
# Diccionario
# valor = {}
# resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
# valor = {'nombre': 'Juan', 'apellido': 'Perez'}
# resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

variable = 10
if bool(variable):
    print('Regreso verdadero')
else:
    print('Regreso falso')

if variable:
    print('Regreso verdadero')
else:
    print('Regreso falso')

while variable:
    print('Ejecucion ciclo while')
    break
else:
    print('fin ciclo while')
