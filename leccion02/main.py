"""
operandoA = 3
operandoB = 4
suma = operandoA + operandoB
#print('El resultado de la suma es ', suma)

# usando la interpolacion para imprimir
print(f'El resultado de la suma es: {suma}')

resta = operandoB - operandoA
print(f'El resultado de la resta es: {resta}')

multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicacion es: {multiplicacion}')

division = operandoA / operandoB
print(f'El resultado de la division es: {division}')
division = operandoA // operandoB
print(f'Resultado tipo entero: {division}')

modulo = operandoA % operandoB
print(f'resultado residuo division modulo: {modulo}')

exponente = operandoA ** operandoB
print(f'El resultado del exponente es: {exponente}')
"""
# tarea realizar un programa para calcular area y perimetro de un rectangulo
# piden que existan dos inputs: un alto y un ancho
# las formulas son: Area= alto * ancho y perimetro = (alto + ancho) *2

alto = int(input('Cual sera el alto de tu rectangulo: '))
ancho = int(input('Cual sera el ancho de tu rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'El area de tu rectangulo es {area}')
print((f'El perimetro de tu rectangulo es {perimetro}'))