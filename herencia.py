# Programa que hará las operaciones de cuadrado y de rectangulo heredando
# los comportamientos:
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura 

# La subclase de Rectangulo va a ser Cuadrado por lo que será importante 
# inicializar la clase Cuadrado con la superclase entre parentesis (Rectangulo).
# Esto se lee, la clase Rectangulo extiende a Cuadrado.

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
    # La subclase se inicializa como cualquier clase con la diferencia que se 
    # llama a la superclase con la palabra: "super", de esta manera obtenemos 
    # la referencia de Rectangulo (superclase) y podemos llamar a su constructor.


if __name__ == '__main__':
    rectangulo = Rectangulo(base = 3, altura = 4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado = 5)
    print(cuadrado.area()) 
    # Notar que podemos ejecutar el método área de cuadrado sin haber sido definido
    # en la clase, esto pasa porque estamos heredando el método de Rectangulo.