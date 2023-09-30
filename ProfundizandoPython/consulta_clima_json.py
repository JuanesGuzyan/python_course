"""
respuesta = urllib.request.urlopen('http://globalmentoring.com.mx/api/clima.json')
# print(respuesta)
cuerpo_respuesta = respuesta.read()
# print(cuerpo_respuesta)
# Procesamos la respuesta json
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
# print(json_respuesta)
# Ejercicio 1. Acceder a la descripcion del clima
# descripcion_clima = json_respuesta.get('clima')[0].get('descripcion')
descripcion_clima = json_respuesta['clima'][0]['descripcion']
print(descripcion_clima)
# Ejercicio 2. Mostrar la temperatura minima y maxima
temp_min = json_respuesta.get('principal').get('temp_min')
print(f'Temperatura minima: {temp_min}')
temp_max = json_respuesta.get('principal').get('temp_max')
print(f'Temperatura maxima: {temp_max}')
"""
