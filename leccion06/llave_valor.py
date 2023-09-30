"""
def listarTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

# la llave (key) no lleva comillas, y el valor puede ser cualquier tipo de dato
listarTerminos(IDE='Integrated Development Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')
"""


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos')
# pasa a ser una tupla con los parentesis y una lista con corchetes
desplegarNombres([10, 11])
