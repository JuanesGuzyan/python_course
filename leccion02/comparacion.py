"""
a = 4
b = 2
# si son iguales
resultado = (a == b)
print(f'Resultado == : {resultado}')

# si son diferentes
resultado = (a != b)
print(f'Resultado != : {resultado}')

# Mayor que
resultado = a > b
print(f'Resultado > : {resultado}')

# mayor o igual
resultado = a >= b
print(f'Resultado >= : {resultado}')

# menor que
resultado = a < b
print(f'Resultado < : {resultado}')

# menor o igual que
resultado = a <= b
print(f'Resultado <= : {resultado}')
"""

# ejercicio

a = int(input('Escribe un valor numerico: '))

# print(a % 2)
if a % 2 == 0:
    print(f'El valor de a {a} es un numero par')
else:
    print(f'El valor de a {a} es un numero impar')