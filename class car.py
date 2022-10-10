class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        #Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        #"""Exibe uma frase que mostra a milhagem do carro."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        #"""Define o valor de leitura do hodômetro com o valor especificado."""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        #"""Soma a quantidade especificada ao valor de leitura do hodômetro."""
        self.odometer_reading += miles

class EletricCar(Car):
        #"""Representa aspectos específicos de veículos elétricos."""
    def __init__(self, make, model,year):
        #"""Inicializa os atributos da classe pai."""
        super().__init__(make, model, year)

my_tesla = EletricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
