from NumerosIdenticosException import NumerosIdenticosException

resultado = None
# a = 10
# b = 0

try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
        raise NumerosIdenticosException('numeros identicos')
    resultado = a/b
except ZeroDivisionError as zde:
    print(f'ZeroDivisionError - Ocurrio un error: {zde}, type: {type(zde)}')
except TypeError as te:
    print(f'TypeError - Ocurrio un error: {te}, type: {type(te)}')
except ValueError as Ve:
    print(f'ValueError - Ocurrio un error: {Ve}, type: {type(Ve)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}, type: {type(e)}')
else:
    print('No se arrojo ninguna excepcion')
finally:
    print(f'Ejecucion del bloque finally')
# bloque else / finally son opcionales
# bloque finally siempre se va a ejecutar independientemente si se lanza una excepcion, para avisar al usuario o menos
# uso de recursos
# bloque else se ejecuta si no se realiza una excepcion del bloque
# ZeroDivisionError o Except, la idea es capturar excepciones a un nivel generico
# Primero van clases especificas y luego mas genericas en el bloque try/except
print(f'Resultado: {resultado}')
print('Continuemos...')
