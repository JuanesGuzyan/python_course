# aqui se ejecuta el polimorfismo
from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)
    # no es recomendable que los metodos tengan muchas validaciones para validar tipos de datos
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


# lo que hacemos es crear una variable llamada empleado que apunta a un objeto que es una instancia de la clase empleado
empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)
