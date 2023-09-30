# Profundizando en diccionarios

# los diccionarios guardan un orden (a diferencia de un set)
diccionario = {'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 28}
print(diccionario)
# los dic son mutables, pero las llaves deben ser inmutables
# diccionario = {(1, 2): 'Valor1'}
print(diccionario)

# Se agrega una llave si no se encuentra
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario (si ya existe, se reemplaza)
diccionario['Nombre'] = 'Juan Carlos'
print(diccionario)

# recuperar elementos de un diccionario - indicando una llave
print(diccionario['Nombre'])
# Si no encuentra la llave lanza una excepcion
# metodo get recupera una llave, y si no existe no lanza excepcion
# ademas podemos regresar un valor en caso que no exista la llave
print(diccionario.get('Nombre', 'No se encontro la llave'))
print(diccionario)

# setdefault si modifica el diccionario, ademas se puede agregar un valor por default
nombre = diccionario.setdefault('Nombre', 'Valor por default')
print(nombre)

# Imprimir con pprint
from pprint import pprint as pp
# help(pp)
pp(diccionario, sort_dicts=False)
