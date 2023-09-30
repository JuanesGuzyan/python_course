# sintaxis de range(inicio<opcional>, fin<requerido>, incremento<opcional>

# Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
for i in range(11):
    if i % 3 != 0:
        continue
    print(f'Valor: {i}')

# Ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimelos
maximo1 = 6
contador = 2

while contador <= maximo1:
    print(contador)
    contador += 1
else:
    print('Fin del algoritmo')

"""
el instructor realizó lo siguiente:

rango = range(2,7)
for i in rango:
    print(i)
"""
# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1

minimo = 3
maximo = 10

while minimo <= maximo:
    print(minimo)
    minimo += 2
else:
    print('Fin del algoritmo')

"""
rango = range(3,11,2)
for i in rango:
    print(i)
"""