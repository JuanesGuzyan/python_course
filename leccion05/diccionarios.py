# lado izq key, lado derecho value
# no es posible agregar llaves duplicadas si agregamos una llave existente sobreescribe la llave con el nuevo valor
# (key, value)
diccionario = {
    # cualquier tipo inmutable se puede usar como llave (int, float, bool, str, etc)
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)

# largo de los elementos
print(len(diccionario))
# acceder a un elemento (key)
print(diccionario['IDE'])
# otra forma de recuperar un elemento
print(diccionario.get('OOP'))
# modificar elementos en un diccionario
diccionario['IDE'] = 'integrated development environment'
print(diccionario)
# recorrer los elementos
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# comprobar existencia de algún elemento
print('IDE' in diccionario)

# agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# remover un elemento
diccionario.pop('PK')
print(diccionario)
# limpiar
diccionario.clear()
print(diccionario)

# eliminar el diccionario, variable de diccionario
del diccionario
print(diccionario)