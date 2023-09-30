a = True
b = False
# resultado = a and b
# print(resultado)

resultado = a or b
print(f'este es de or : {resultado}')

resultado = not a
print(f'este es de not: {resultado}')

# ejercicio de rango
"""
valor = int(input('Escribe el valor: '))
valorMinimo = 0
valorMaximo = 5

# dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)
dentroRango = valor >= valorMinimo and valor <= valorMaximo

if dentroRango:
    print(f'El numero {valor} esta dentro del rango')
else:
    print(f'El numero {valor} no esta dentro del rango')
"""

# ejericicio con operador "or"

vacaciones = False
diaDescanso = False
"""
# con cualquiera de los 2 valores sea True puede asistir al juego dado que or solamente necesita un True, no los dos
if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('No puede asistir al juego')
"""
# ejercicio not

if not (vacaciones or diaDescanso):
    print('No puede asistir al juego')
else:
    print('Puede asistir al juego')
