# profundizando listas
# listas son mutables
nombres1 = ['Juan', 'Pedro', 'Marcos']
nombres2 = 'Lucas Maria Elena'.split()
# sumar listas
print(f'Sumar listas: {nombres1 + nombres2}')
# Extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Extender la lista1 con la lista2: {nombres1}')

# Lista de numeros
numeros1 = [10, 40, 15, 4, 20, 90, 4]
print(f'Lista original: {numeros1}')
# Obtener el indice del primer elemento encontrado en una lista
# help(list.index)
print(f'Indice 4: {numeros1.index(4)}')

# Invertir Orden de los elementos de una lista
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

# Ordenar los elementos
numeros1.sort()
print(f'Lista ordenada: {numeros1}')

# Ordenar de manera descendente
numeros1.sort(reverse=True)
print(f'Lista ordenada descendente: {numeros1}')

# Obtener el valor min y max de una lista
print(f'valor min: {min(numeros1)}')
print(f'valor max: {max(numeros1)}')
# Copiar los elementos de una lista
numeros2 = numeros1.copy()
print(f'Es la misma referencia: {numeros1 is numeros2}')
print(f'Mismo contenido: {numeros1 == numeros2}')
# help(list.copy)
# Podemos usar el constructor de la lista
numeros2 = list(numeros1)
print(f'Es la misma referencia: {numeros1 is numeros2}')
print(f'Mismo contenido: {numeros1 == numeros2}')
# slicing
numeros2 = numeros1[:]
print(f'Es la misma referencia: {numeros1 is numeros2}')
print(f'Mismo contenido: {numeros1 == numeros2}')

# Multiplicar listas
lista_multiplicacion = 5 * [[2, 5]]
print(lista_multiplicacion)
print(f'Misma referencia: {lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Mismo contenido: {lista_multiplicacion[0] == lista_multiplicacion[1]}')
lista_multiplicacion[2].append(10)
print(lista_multiplicacion)

# Matrices
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Matriz original: {matriz}')
print(f'Renglon 0, Columna 0: {matriz[0][0]}')
print(f'Renglon 2, Columna 2: {matriz[2][2]}')
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')

lista_listas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 45, 61, 70]]
lista_listas.sort(key=len)
print(f'Ordenar lista: {lista_listas}')

# built-in hacen parte del lenguaje de python - sorted es built-in
# help(sorted)
nombres1 = ['Juan Carlos', 'karla', 'Pedro', 'Maria']
nombres1 = sorted(nombres1)
print(nombres1)
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)
# ordenar por la cantidad de caracteres (largo)
nombres1 = sorted(nombres1, key=len)
print(nombres1)
# built-in reversed
nombres1 = reversed(nombres1)
print(list(nombres1))
