"""
cadena = 'Hola'

# for = para o por cada elemento, en otros lenguajes se conoce como for each
for letra in cadena:
    print(letra)
else:
    print('Fin ciclo for')
"""
# break en python
"""
for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
        # util cuando buscamos un elemento en una lista de datos, break rompe el ciclo cuando encontramos el elemento buscado
else:
    print('Fin del ciclo for')
"""
# continue en python

# for i in range(6):
#    if i % 2 == 0:
#        print(f'Valor: {i} ')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')

# ejemplo más claro del continue en caso dado olvide
x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)