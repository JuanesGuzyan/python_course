# Orden de inicializacion de objetos
class Padre:
    def __init__(self):
        print('Inicializador Padre')

    def metodo(self):
        print('Metodo Padre')


class Hijo(Padre):
    # Se manda a llamar el metodo __init__ de la clase padre
    # Siempre y cuando la clase hija no defina su propio metodo init
    # Definimos el metodo init
    def __init__(self):
        # De manera opcional podemos llamar al metodo init de la clase padre (super)
        super().__init__()
        print('Inicializador Hijo')

    # Sobreescribimos el metodo heredado de la clase padre
    def metodo(self):
        print('Metodo sobreescrito hijo')
        super().metodo()


# padre1 = Padre()
# padre1.metodo()
hijo1 = Hijo()
hijo1.metodo()
