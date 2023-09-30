# Profundizar en set
# Un set es una coleccion de elementos unicos y es mutable
# Los elementos de un set deben ser inmutables
conjunto = {'Juan', True, 18.0}
print(conjunto)
# Set vacio
# onjunto = {}
# print(type(conjunto)) Genera un diccionario vacio
# Set vacio Correcto
conjunto = set()
print(conjunto)
print(type(conjunto))
# Mutable
conjunto.add('Juan')
print(conjunto)
# Contiene valores unicos
conjunto.add('Juan')
print(conjunto)
# Crear un set a partir de un iterable
conjunto = set([4, 5, 7, 8, 4])
print(conjunto)
# Podemos agregar mas elementos o incluso otro set
conjunto2 = {100, 200, 300, 300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20, 30, 40, 40])
print(conjunto)

# Copiar un set (Copia poco profunda, Solo copia referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# Verificar igualdad
print(f'Es igual en contenido: {conjunto == conjunto_copia}')
print(f'Es igual en referencia: {conjunto is conjunto_copia}')

# Operaciones de conjuntos con set
# Personas con distintas caracteristicas
pelo_negro = {'Juan', 'Karla', 'Pedro', 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marcos'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'Maria'}
# Union - Unir 2 sets por completo - Todos con ojos cafe y pelo rubio
# no se repiten los elementos de un set
print(ojos_cafe.union(pelo_rubio))
# Invertir el orden con mismo resultado
print(pelo_rubio.union(ojos_cafe))
# Interseccion - en ambos conjuntos
# Intersection(conmutativa) - Solo las personas con ojo cafe y pelo rubio
print(ojos_cafe.intersection(pelo_rubio))
# (Difference)No es conmutativa - Elementos de un conjunto que no sean intersectados
print(pelo_negro.difference(ojos_cafe))
# (Diferencia simetrica) Pelo negro u ojos cafe, pero no ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))

# Preguntar si un set esta contenido en otro (subset)
# revisamos si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issubset(pelo_negro))

# Preguntar si un set contiene a otro set (superset)
# revisar si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issuperset(pelo_negro))

# Preguntar si los de pelo negro no tienen pelo rubio (disjoint)
print(pelo_negro.isdisjoint(pelo_rubio))
