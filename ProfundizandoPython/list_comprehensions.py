numeros = range(10)
lista_pares = []

# Creamos una nueva lista con los valores pares multiplicados por si mismos
for numero in numeros:
    # Revisamos si es un numero par
    if numero % 2 == 0:
        lista_pares.append(numero * numero)

print(f'Lista pares: {lista_pares}')

# Hacemos lo mismo pero con list comprehensions
# [expresion for variable in coleccion if condicion]
# La condicion de if es opcional
lista_pares = []
lista_pares = [numero * numero for numero in numeros if numero % 2 == 0]
print(f'Lista de pares con list comprehension: {lista_pares}')

# Un ejemplo similar pero con dos condiciones (las condiciones son opcionales)
# solo se agrega el valor a la lista cuando el valor cumple ambas condiciones
# es decir, debe ser divisible entre 2 y divisible entre 6
pares = [numero for numero in range(50) if numero % 2 == 0 if numero % 6 == 0]
print(f'Numeros divisibles entre 2 y 6: {pares}')

# Agregando if else
lista_pares = []
lista_impares = []
for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)


print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

# El mismo ejercicio pero usando list comprehension
lista_pares = []
lista_impares = []
# [Expresion() - if - else() - for ()]
[lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero) for numero in range(10)]
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

# Lista de listas
lista_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
# Convertimos la lista de listas en un sola lista
lista_simple = [valor for sublista in lista_listas for valor in sublista]
print(f'Lista simple: {lista_simple}')

# Ahora creamos una lista de numeros pares a partir de la lista_listas
# Sin list comprehension, ciclos for anidados
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor % 2 == 0:
            lista_pares.append(valor)
print(f'Lista pares: {lista_pares}')

# Con List Comprehensions, en un sola linea de codigo
# No es necesario separar las lineas, solo es para mejor lectura de codigo
lista_pares = []
lista_pares = [valor
               for sublista in lista_listas
               for valor in sublista
               if valor % 2 == 0]
print(f'Lista pares: {lista_pares}')
