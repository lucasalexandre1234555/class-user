from datetime import datetime
data = datetime.now()

data=data.strftime("%d/%m/%Y")
print(data)

class User():
    def __init__(self,first_name,last_name,age,join_date,location):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.join_date=join_date
        self.location=location

    def describe_user(self):
        print(f'Name:{first_name} {last_name}\nIdade:{age}\npaís:{location}\ncadastrou-se em:{join_date}')

    def greet(self):
        print(f"\nBem vindo(a) {first_name} {last_name}!!")

first_name=input('nome:').capitalize()
last_name=input('sobrenome:').capitalize()
age=input('idade:')
join_date=data
location=input("seu pais:").capitalize()
User = User(first_name,last_name,age,join_date,location)
User.describe_user()
User.greet()
