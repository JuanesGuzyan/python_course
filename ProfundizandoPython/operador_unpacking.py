# * desempaquetar
numeros = [1, 2, 3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')


# desempaquetando al momento de pasar un parametro a una funcion
def sumar(a, b, c):
    print(f'Resultado: {a + b + c}')


sumar(*numeros)

# Extraer algunas partes de una lista
mi_lista = [1, 2, 3, 4, 5, 6]
a, *b, c, d = mi_lista
print(a, b, c, d)

# Unir lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [lista1, lista2]
print(f'Lista de listas: {lista3}')
lista3 = [*lista1, *lista2]
print(f'Unir listas: {lista3}')

# Unir diccionarios
dic = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5}
dic3 = {**dic, **dic2}
print(f'Unir diccionarios: {dic3}')

# Construir una lista a partir de un str
lista = [*'HelloWorld']
print(lista)
print(*lista, sep='')
