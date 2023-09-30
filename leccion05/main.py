# lista de tipos de string o cualquier tipo de dato que exista en python
# el primer elemento de una lista tiene un índice, generalmente comienzan en 0

# definir una lista de tipo str
nombres = ['Juan', 'Karla', 'Ricardo', 'María']
# imprimir la lista nombres
print(nombres)
# acceder de manera individual a los elementos de la lista
print(nombres[0])
print(nombres[1])
# acceder a los elementos de forma inversa, recorrer la lista
print(nombres[-1])
print(nombres[-2])

# imprimir un rango
print(nombres[0:2])  # sin incluir el indice 2

# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])

# Desde el indice indicado hasta el final
print(nombres[1:])

# cambiar un valor
nombres[3] = 'Pedro'
print(nombres)

# iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No hay más nombres en la lista')

# preguntar el largo de una lista
print(len(nombres))

# agregar un elemento
nombres.append('Lorenzo')
print(nombres)

# insertar un elemento en un indice en especifico
nombres.insert(1, 'Octavio')
print(nombres)

# remover un elemento
nombres.remove('Octavio')
print(nombres)

# remover el último valor agregado
nombres.pop()
print(nombres)

# eliminar un indice
del nombres[0]
print(nombres)

# limpiar la lista
nombres.clear()
print(nombres)

# eliminar la lista por completo de memoria
del nombres
print(nombres)
