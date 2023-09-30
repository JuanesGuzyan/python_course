# definir una funcion dentro de otra

def calculadora(a, b, operacion='sumar'):
    # Definir .funcion anidada
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        return a / b

    # LLamada a la funcion anidada
    if operacion == 'sumar':
        print(f'Resultado sumar: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado restar: {restar(a, b)}')
    elif operacion == 'multiplicar':
        print(f'Resultado multiplicar: {multiplicar(a, b)}')
    elif operacion == 'dividir':
        print(f'Resultado dividir: {dividir(a, b):.2f}')

calculadora(5, 6)
calculadora(5, 6, operacion='dividir')
calculadora(5, 6, operacion='multiplicar')
