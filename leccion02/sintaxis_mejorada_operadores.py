"""

edad = int(input('Introduce tu edad: '))

if (20 <= edad < 30 ) or (30 <= edad < 40):
    print(f'Tu edad {edad} esta dentro del rango de los (20\'s) o (30\'s)')
else:
    print(f'No esta dentro del rango de los (20\'s) o (30\'s)')


# ejercicio propuesto en clase:

Instrucciones de tareas:
Solicitar al usuario dos valores, y determinar cual numero es el mayor
Solicitor al usuario dos valores:
numero1 (int)
numero2 (int)

Se debe imprimir el mayor de los dos numeros (la salida debe ser identico a la que sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es:<numeroMayor>

"""
numero1 = int(input('Inserta un valor numerico: '))
numero2 = int(input('Inserta un segundo valor numerico: '))

if numero1 > numero2:
    print(f'El numero {numero1} es mayor que {numero2}')
else:
    print(f'El numero {numero2} es mayor que {numero1}')