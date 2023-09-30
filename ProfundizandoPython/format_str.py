nombre = 'Juan'
edad = 28
sueldo = 3000
# mensaje = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)

# mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)

# mensaje = 'Sueldo {2:.2f} Nombre {0} Edad {1} '.format(nombre, edad, sueldo)
# print(mensaje)

# Profundizando con format
# mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# print(mensaje)

# Otra forma
diccionario = {'nombre': 'Iván', 'edad': 35, 'sueldo': 8000.00}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)
