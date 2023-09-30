class Cubo:
    def __init__(self, ancho, profundo, alto):
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto

    def calcular_volumen(self):
        return self.ancho * self.profundo * self.alto


print('Bienvenido al programa para calcular volumen de un cubo')
ancho = int(input('Proporcione el ancho: '))
profundo = int(input('Proporcione el valor profundo: '))
alto = int(input('Proporcione el alto: '))

cubo1 = Cubo(ancho, profundo, alto)
print(f'El volumen del cubo proporcionado es: {cubo1.calcular_volumen()}')
