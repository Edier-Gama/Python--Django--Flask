#Decomponer es básicamente partir una clase en varias partesitas mas pequeñas
# Aqui partimos de la clase carro e hicimos varias funciones mas. Decompusimos.

class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._engine = Engine()


    def state(self):

        self.on == True
        self.off == False


    def movement(self):

        self.movement = Car.state()

        if Car.state() == True:
            print('Your max velocity is 80km/h')
        else:
            Car.state() == False
            print('You are off')        

class Engine:

    def __init__(self, cilindros, type, movement):

        self.cilindros = cilindros
        self.type = type
        self.temperature = 0
         
    def inyectar_gasolina(self, cantidad):

        self.cantidad = cantidad

