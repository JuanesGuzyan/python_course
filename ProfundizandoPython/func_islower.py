mensaje = 'Hello World'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())

# alinear cadenas
# centrar un str - center
titulo = 'Sitio web de globalmentoring.com.mx'
# print(len(titulo))
# print(titulo.center(50, '*'))
# print(len(titulo.center(50, '*')))
print(titulo.center(len(titulo)+10, '-'))
# print(titulo.ljust(50, '*'))
# ljust - alinea a izquierda
print(titulo.ljust(len(titulo)+10, '*'))
# rjust - alinea a derecha
# print(titulo.rjust(50, '*'))
print(titulo.rjust(len(titulo)+10, '*'))

# reemplazar contenido en un str
# print(contenido.replace(' ','-'))

# Eliminar caracteres al inicio y final de un str - strip
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original:', titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada:', titulo, len(titulo))
titulo = '*** GlobalMentoring.com.mx ***'.strip('*')
print('Cadena modificada:', titulo)
# lstrip - rstrip
titulo = '*** GlobalMentoring.com.mx ***'.lstrip('*')
print('Cadena modificada:', titulo)
titulo = '*** GlobalMentoring.com.mx ***'.rstrip('*')
print('Cadena modificada:', titulo)

titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print('Cadena modificada:', titulo, len(titulo))
