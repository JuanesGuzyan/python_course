# Scope en ingles - tiempo de vida de una variable
# Alcance de variables
var_global = 'Variable global'


def imprimir():
    # Acceder a una variable global
    global var_global
    print(f'Variable global desde funcion: {var_global}')
    # Definicion de variable local - esta dentro del bloque de codigo
    var_local = 'Variable local'
    print(f'Variable local desde funcion: {var_local}')
    var_global = 'Nuevo valor variable global'

    def funcion_anidada():
        print(f'Variable local dentro de funcion anidada: {var_local}')

    funcion_anidada()


imprimir()
print(f'Variable global fuera funcion: {var_global}')
# No es posible acceder a variables locales fuera del bloque donde se definieron
# variable local se puede usar dentro de bloques internos - anidadas
