# Ejemplo atributos publicos, protegidos, privados
class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado


objecto = MiClase('Valor publico', 'Valor protegido', 'Valor privado')
# Acceso al atributo publico
print(objecto.publico)
# Modificar el valor publico
objecto.publico = 'Nuevo valor publico'
print(objecto.publico)

# Acceso al valor protegido
# Solo dentro de la misma clase o clases hijas
# print(objeto._protegido)
# es posible acceder, pero no es buena practica
# Modificar valor protegido
# objeto._protegido = 'Nuevo valor protegido'
# print(objeto._protegido)
# se puede realizar la accion pero no es buena practica
# Acceder al valor privado
# No es posible acceder directamente
# pero, convierte: objeto._clase__atributo_privado
# print(objecto._MiClase__privado)
# se puede acceder, pero no es buena practica
# Modificar valor privado
# objecto._MiClase__privado = 'Nuevo valor privado'
# print(objecto._MiClase__privado)
