print('Proporcione los siguientes datos del libro para el envío')

tituloLibro = input('Proporcione el titulo del libro: ')
idLibro = int(input('Proporcione el ID del libro: '))
precioLibro = float(input('Proporcione el precio del libro: '))
envioLibro = input('El envio será gratuito? (True/False): ')

if envioLibro == 'True':
    envioLibro = True
elif envioLibro == 'False':
     envioLibro = False
else:
    envioLibro = 'Valor incorrecto, debe escribir True / False'

print(f'''
    Nombre del libro: {tituloLibro}
    ID del libro: {idLibro}
    Precio del libro: {precioLibro}
    Envío gratuito?: {envioLibro}
''')
