class Persona:
    contador_personas = 0

    # en ocasiones podria ser contraproducente, no se utilice de manera externa
    @classmethod
    def _generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    # inicializar la variable, la variable de clase de arriba se comparte para todos los objetos de nuestra clase de
    # tipo persona
    def __init__(self, nombre, edad):
        self.id_persona = Persona._generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: [{self.id_persona} {self.nombre} {self.edad}]'


persona1 = Persona('Juan', 28)
print(persona1)

persona2 = Persona('Pedro', 25)
print(persona2)
persona3 = Persona('Eduardo', 30)
print(persona3)
persona4 = Persona('Maria', 35)
print(persona4)
print(f'Valor contador personas: {Persona.contador_personas}')
