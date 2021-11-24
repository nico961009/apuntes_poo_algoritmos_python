# Vamos a decomponer un automóvil.
# Este es solo un programa de juguete, solo para entender el concepto.

class Automovil:

# Comenzamos con nuestro constructor para inicializar la clase:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo       
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor (cilindros=4) #Este Motor lo estamos jalando de la clase generada abajo.
        # mediante el uso de ._ se denota una clase privada en python. 

    def acelerar(self, tipo= 'despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        
        self._estado = 'en_movimiento'

class Motor:

# En el caso de tipo='gasolina' estamos inicializando un parámetro por default.
# Al ser por defecto o defaut significa que la podemos específicar o no.
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
    
    def inyecta_gasolina(self, cantidad):
        pass

    