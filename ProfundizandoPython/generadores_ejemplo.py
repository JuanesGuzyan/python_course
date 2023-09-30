# Generador de numeros del 1 al 5
def generador_numeros():
    for numero in range(1, 6):
        yield numero
        print('Se reanuda la ejecucion de la funcion')


# Utilizamos el generador
generador = generador_numeros()
print(f'Objeto generador: {generador}')
print(type(generador))

# Consumimos los valores del generador
for valor in generador:
    print(f'Numero producido: {valor}')

# Consumir a demanda
generador = generador_numeros()
try:
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
except StopIteration as e:
    print(f'Error al consumir generador: {e}')

# Otra forma de consumir un generador
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f'Impresion valor generado: {valor}')
    except StopIteration as e:
        print('Se termino de iterar el generador')
        break
