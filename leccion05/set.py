# no tiene orden y no permite elementos duplicados, no es posible modificarlos pero pueden agregar o eliminar
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)

# Conocer el largo de los elementos

print(len(planetas))
# Revisar si un elementos está presente, también se realiza en listas y tuplas
print('Marte' in planetas)

# agregar un elemento
planetas.add('Tierra')
print(planetas)
# No se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
# eliminar elementos posiblemente arrojando un error
planetas.remove('Tierra')
print(planetas)
# eliminar elemento sin arrojar error si no encuentra el elemento
planetas.discard('Júpiter')
print(planetas)
# limpiar set
planetas.clear()
print(planetas)
# eliminar set por completo
del planetas
print(planetas)