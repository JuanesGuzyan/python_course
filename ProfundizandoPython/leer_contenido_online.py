# leer contenido online
from urllib.request import Request, urlopen

palabras = []
request = Request("https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt")  # hacemos el request a la pagina
request.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/97.0.4692.71 Safari/537.36')  # colocamos los headers
with urlopen(request) as response:  # hacemos el open para que se cierre
    mensaje = response.read().decode('utf-8')
    for linea in mensaje:
        palabras_por_linea = linea.split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)
print(palabras)
#    print(mensaje)

# with open('nuevo_archivo.txt', 'w', encoding='utf-8') as archivo:
#    archivo.write(mensaje)
"""
with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    for linea in mensaje:
        palabras_por_linea = linea.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)
print(palabras)

with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    contenido = mensaje.read().decode('utf-8')


contar ocurrencias de una cadena
print(contenido.count('Universidad))

convertir a mayusculas un str
print(contenido.upper())
print(contenido)

lower convierte a minusculas un str
print(contenido.lower())

# buscamos la cadena python
print('Existe python?:','python'.lower() in contenido.lower())
print('Existe python?:','python'.upper() in contenido.upper())

# startswith - inicia con
print(contenido.startswith('En GlobalMentoring.com.mx'))

# endswith - termina con
print(contenido.lower().endswith('globalmentoring.com.mx'.lower()))
"""
