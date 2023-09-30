# clases y objetos
# una clase es una plantilla
# la clase posee atributos y metodos - un objeto es una instancia de una clase

class Persona:
    # palabra reservada para que cree la funcion pero no va a tener ningún contenido todavía pass
    # no es común asignar valores por default a los atributos
    # double underscore = dunder - self es una referencia al objeto en si mismo
    # atributos = izquierda - parámetros derecha
    # self tambien puede llamarse this
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        #        print('Llamando metodo get nombre')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        #        print('Llamando metodo set nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self.edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

# mejores practicas con python
if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28, )
    persona1.nombre = 'Pedro'
    persona1.apellido = 'Lara'
    persona1.edad = 27
    persona1.mostrar_detalle()

    print(__name__)
# main es el módulo principal
# si omitimos el metodo set entonces se dice que es una variable de solo lectura si solamente tenemos property
# A esto se le conoce como atributos públicos
# persona1.nombre = 'Juan Carlos'
# A esto se le conoce como atributo encapsulado
# persona1._nombre = 'Juan Carlos'
# persona1.mostrar_detalle()
# decorador property hace que entremos al metodo como si fuera un atributo
# get para obtener / recuperar
# set para colocar/modificar
# se puede utilizar doble guion bajo para restringir su uso, no se utiliza tanto y simplemente se encontrará un
# guion abajo
# persona1.mostrar_detalle()
# persona1.telefono = '3141941'
# Persona.mostrar_detalle(persona1)
# un constructor es un método para construir un objeto
# un metodo es igual que una funcion, pero se le llama metodo porque se asocia
# a una clase
# UML se utiliza para documentar cuando se trabaja con objetos
