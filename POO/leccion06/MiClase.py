class MiClase:
    # se va a asociar con la clase y se va a poder compartir con todos los objetos
    variable_clase = 'Valor variable clase'

    # variable de instancia, cada objeto tiene su propio valor
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # metodos estaticos, vamos a utilizar el nombre de la clase primero, no pueden acceder
    # a los metodos de instancia ni variables de instancia
    # contexto estatico = cuando trabajamos con la clase y contexto dinamico = cuando trabajamos con los objetos
    # un metodo estatico no recibe informacion de la clase
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # metodo de clase, si reciben informacion de la clase en si misma.
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    # debido a que es del contexto dinamico podemos acceder al contexto estatico
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)


miObjeto1 = MiClase('Valor variable instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()

MiClase.metodo_clase()
# MiClase.metodo_estatico()

# print(MiClase.variable_clase)

# miClase = MiClase('Valor variable instancia')
# print(miClase.variable_instancia)

# el objeto puede acceder a la variable de clase que esta cargada a la memoria
# print(miClase.variable_clase)

# Variable al vuelo. no es tan comun, pero es posible porque python es dinamico
# MiClase.variable_clase2 = 'Valor variable clase 2'

# miClase2 = MiClase('Otro valor de variable de instancia')
# print(miClase2.variable_instancia)
# print(miClase2.variable_clase)

# desde la misma clase
# print(MiClase.variable_clase2)
# desde el objeto
# print(miClase.variable_clase2)
# desde el objeto 2, las clases tambien son objetos en python
# print(miClase2.variable_clase2)
# creacion de variables clase al vuelo = en cualquier momento
