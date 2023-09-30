"""
Ejercicio calculadora de impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto
aplicado.
Fórmula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""
"""
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total


# Ejecutamos la funcion
pago_sin_impuesto = float(input('Proporcione el pago sin impuestos: '))
impuesto = float(input('Proporcione el monto del impuesto: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')
"""

"""
Ejercicio: Convertidor de temperatura
Realizar dos funciones para convertir de grados celsius a farenheit y
viceversa
"""


def grado_celsius(temperatura):
    # podemos usar el return en la linea 28, return temperatura * 9/5 + 32
    grado_farenheit = (temperatura * 9 / 5) + 32
    return grado_farenheit


# Ejecutamos la funcion
temperatura = float(input('Proporcione el grado Celsius: '))
convertido = grado_celsius(temperatura)
print(f'Grados Farenheit {convertido:.3f}')


# convertidor de farenheit a celsius
def farenheit_degree(temperature):
    celsius_degree = (temperature - 32) * 5 / 9
    return celsius_degree


# Ejecutamos la funcion
temperature = float(input('Please provide farenheit degree: '))
degree = farenheit_degree(temperature)
print(f'{degree:.3f} Farenheit degrees')
