class Persona:

    def __init__(self, nombre):
        self.nobre = nombre

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    # Aquí se hace una modificación al comportamietno desde la clase persona.
    # Esta es la forma de aplicar el polimosrfismo.
    def avanza(self):
        print('Ando moviendome en mi bicicleta')

def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()

if __name__ == '__main__':
    main()