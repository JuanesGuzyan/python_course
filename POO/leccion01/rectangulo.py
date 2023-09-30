class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


print('Bienvenido al programa calcula el area del rectangulo')
base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f'Area Rectangulo: {rectangulo1.calcular_area()}')
