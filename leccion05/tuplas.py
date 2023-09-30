# Definir una tupla
frutas = ('Naranja', 'Plátano', 'Guayaba')
print(frutas)
# Saber el largo de una tupla
print(len(frutas))

# Acceder a un elemento
print(frutas[0])

# Navegación inversa
print(frutas[-2])

# Acceder a un rango de valores
print(frutas[0:1]) # sin incluir el último índice, para ser una tupla el último valor debe tener una coma al final al ser solamente un elemento

# Recorrer elementos de una tupla
for fruta in frutas:
    print(fruta, end=' ')
# cambiar valor tupla no es posible, es inmutable
# frutas[0] = 'Pera'
# print(frutas)

# conversiones entre tupla y lista o viceversa

frutalista = list(frutas)
frutalista[0] = 'Pera'
frutas = tuple(frutalista)
print('\n', frutas)

# eliminar la tupla por completo
del frutas
print(frutas)