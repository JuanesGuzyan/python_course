"""
edad = int(input('Coloca tu edad: '))
edadMinima = 20
edadMaxima = 30

if edad >= edadMinima and edad <= edadMaxima:
    print(f'{edad} años se encuentra dentro del rango')
else:
    print(f'{edad} años no se encuentra dentro del rango')
"""
# ejercicio por el instructor

edad1 = int(input('Introduce tu edad: '))

# veintes = edad1 >= 20 and edad1 < 30
# print(veintes)
# treintas = edad1 >= 30 and edad1 < 40
# print(treintas)

if (edad1>= 20 and edad1 < 30) or (edad1 >= 30 and edad1 < 40):
    # usando caracter de escape
    print(f'Tu edad ({edad1}) esta dentro del rango de los (20\'s) o (30\'s)')
    # if anidado
#  if veintes:
#        print("Esta dentro de los 20's")
#   elif treintas:
#        print("Esta dentro de los 30's")
#    else:
#        print('Fuera de rango')
else:
    print("No esta dentro de los 20's ni 30's")

