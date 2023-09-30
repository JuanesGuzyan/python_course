# caracteres bytes
caracteres_en_bytes = b'Hola World'
print(caracteres_en_bytes)

mensaje = b'Universidad Python'
print(mensaje[0])
print(chr(mensaje[0]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

# Convertir str a bytes
string = 'Programación con Python'
print(f'String original: ', string)
bytes = string.encode('UTF-8')
print('bytes codificado:', bytes)
# convertir bytes a str
string2 = bytes.decode('UTF-8')
print(f'String decodificado:', string2)
print(string == string2)
