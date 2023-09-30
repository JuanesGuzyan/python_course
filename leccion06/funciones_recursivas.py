# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120
"""
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

numero = int(input('Introduce un número para conocer su factorial: '))
resultado = factorial(numero)
print(f' El factorial de {numero} es {resultado}')
"""
"""
Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, 
debe imprimir:
5
4
3
2
1

En caso de pasar el valor de 3, debe imprimir:
3
2
1

No debe pasar a imprimir numeros negativos
"""

def imprimir_numero_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_numero_recursivo(numero - 1)
    elif numero == 0:
        return
    elif numero < 0:
        print('Valor incorrecto')


imprimir_numero_recursivo(5)