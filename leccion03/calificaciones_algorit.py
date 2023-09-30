print('Sistema de calificaciones S.A.S')

puntuacion = int(input('Proporciona la puntuación obtenida: '))

calificacion = None

if 9 <= puntuacion <= 10:
    calificacion = 'La nota es A, felicitaciones'
elif 8 <= puntuacion < 9:
    calificacion = 'La nota es B'
elif 7 <= puntuacion < 8:
    calificacion = 'La nota es C'
elif 6 <= puntuacion < 7:
    calificacion = 'La nota es D'
elif 0 <= puntuacion < 6:
    calificacion = 'La nota es F, puedes mejorar'
else:
    calificacion = 'Valor incorrecto..'

print(f'Obtuviste una {calificacion}')
