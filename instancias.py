class Coordenada:

    # Constructor en python:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Aquí estamos introducciendo la formula para el cálculo de distancias por medio
    # del método ecluidiano.
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

# En la siguiente línea de código estamos utilizando el método "distancia" de nuestra clase "Coordenada" para el calculo de la
# distancia.
    print(coord_1.distancia(coord_2))

# se utiliza el siguiente método que nos permite determinar si "coord_2" es instancia de la clase "Coordenada".
    print(isinstance(coord_2, Coordenada))

