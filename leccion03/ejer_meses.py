mes = int(input('Proporciona un mes del año (1-12): '))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes incorrecto'
print(f'Para el {mes} la estación es: {estacion}')

# ejercicio para clasificar etapas segun edad del usuario

edad = int(input('Proporciona tu edad: '))

etapa = None

if 0 <= edad < 10:
    etapa = 'La infancia es increíble'
elif 10 <= edad < 20:
    etapa = 'Muchos cambios y mucho estudio'
elif 20 <= edad < 30:
    etapa = 'Amor y comienza el trabajo'
else:
    etapa = 'Etapa no identificada'

print(f'Con {edad} años: {etapa}')