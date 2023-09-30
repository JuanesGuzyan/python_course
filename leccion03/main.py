""""
condicion = True

if condicion == True:
    print('Condición verdadera')
# de lo contrario si condicion es false entonces condicion es falsa, se agrega de manera opcional
elif condicion == False:
    print('Condición falsa')
else:
    print('Condición no reconocida')
# ejercicio para convertir valor numerico a texto

numero = int(input('Proporciona un valor entre 1 y 3: '))

numeroTexto = ''
if numero == 1:
    numeroTexto = 'Número uno'
elif numero == 2:
    numeroTexto = 'Número dos'
elif numero == 3:
    numeroTexto = 'Número tres'
else:
    numeroTexto = 'Valor fuera del rango'

print(f'Número proporcionado: {numero} - {numeroTexto}')
"""
condicion = True
# se usa cuando el código es pequeño solamente se usa else y if, no se puede usar elif: sintaxis simplificada
print('Condición es verdadera') if condicion else ('Condición es falsa')

