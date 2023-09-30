# polimorfismo, multiples formas en tiempo de ejecucion dependiendo del objeto
# solamente se ejecuta 1
# la variable var puede apuntar a cualquier tipo de objeto y ejecutar cualquier otro metodo del objeto al que apunta
# no necesariamente tiene que tener herencia o relacion entre clases

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'

    def mostrar_detalles(self):
        return self.__str__()