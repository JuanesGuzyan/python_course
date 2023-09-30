# Generadores
# Es una funcion especial, retorna una secuencia de valores
# suspende la ejecucion de la funcion yield (producir) (no se usa return)
def generador():
    yield 1
    print('Se reanuda la ejecucion')
    yield 2
    print('Se reanuda la ejecucion')
    yield 3


# Yield = Producir - Consumimos el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
# Si tratamos de consumir mas valores de lo que se produce el generador
# lanza un error de StopIteration
# Consumiendo los valores del generador con un ciclo for
for valor in generador():
    print(f'Numero generado: {valor}')
