# Profundizando

# help(str.join)

tupla_str = ('Hola', 'World', 'Universidad', 'Python')
mensaje = ' '.join(tupla_str)
print(mensaje)

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
print(mensaje)

cadena = 'HolaWorld'
mensaje = '.'.join(cadena)
print(mensaje)

diccionario = {'nombre':'Juan', 'apellido':'Perez', 'edad':'18'}
llaves = '-'.join(diccionario.keys())
valores= '-'.join(diccionario.values())
print(f'llaves: {llaves}, type: {type(llaves)}')
print(f'valores: {valores}, type: {type(valores)}')
