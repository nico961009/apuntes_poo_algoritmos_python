class Lavadora:

# En este caso no vamos a utilizar la función de inicialización por lo que se 
# le coloca un "pass".
    def __init__(self):
        pass

# Con la siguiente función ya tendremos la interfaz con la cual vamos a interactuar, en este caso
# esta función representa nuestro método público:

    def lavar(self, temperatura='caliente'):
    # A continuación se define como privado los siguientes métodos ya que para el usuario no es relavente
    # lo que este únicamente desea es definir la temperatura dar en lavar y que la lavadora trabaje.
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Añadiendo jabón')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__ == '__main__':
# Forma de instanciar la clase lavadora:

    lavadora = Lavadora()
    # Al no colocar ningún parámetro dentro de la clase por defecto será: 'Caliente' como se definió aneriormente.

    # Con la siguiente línea de código llamamos al método público:
    lavadora.lavar()