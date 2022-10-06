from datetime import datetime
horaatual = datetime.now()

horaatual = horaatual.strftime("%H%M")
horario = list(horaatual)
horario.insert(2, ':')
print(''.join(horario))
horaatual=int(horaatual)

class restaurant():
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine
        self.number_served=0
        if horaatual >= 800 and horaatual <= 2300:
            self.open=True
        else:
            self.open=False

    def describe(self):
        print(f"{self.name} {self.cuisine} {'está fechado'if not self.open else 'está aberto'}")

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant=restaurant('Burguer King','Hamburgueria')
restaurant.describe()


print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))
