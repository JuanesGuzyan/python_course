# Profundizando

# help(str.split)
"""
cursos = 'Java Python JavaScript Angular Spring Excel'
lista_cursos = cursos.split()
print(f'lista cursos: {lista_cursos}')
print(type(lista_cursos))

cursos_separados_coma = 'Java,Python,JavaScript,Angular,Spring,Excel'
lista_cursos = cursos_separados_coma.split(',')
print(f'lista cursos: {lista_cursos}')
print(len(lista_cursos))

lista_cursos = cursos_separados_coma.split(',', 2)
print(f'lista cursos: {lista_cursos}')
print(len(lista_cursos))
"""
# Dar formato a un str, utilizando parametros condicionales
# nombre = input('Escribe tu nombre: ')
# edad = int(input('Escribe tu edad: '))
# mensaje_con_formato = 'Mi nombre es %s y tengo %d años' % (nombre, edad)
# print(mensaje_con_formato)

persona = ('Karla', 'Gomez', 5000.00)
# mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f' % persona
# print(mensaje_con_formato)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
print(mensaje_con_formato%persona)
