class Car():
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def show(self):
        print(f'I have a {self.name}.')


a = Car('Pride' , 100)        
b = Car("Benz" , 900)

print(a)

################################################

class Car():
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def show(self):
        print(f'I have a {self.name}.')

    def __str__(self): #dunder
        return f"{self.name} - {self.price}"

a = Car('Pride' , 100)        
b = Car("Benz" , 900)

print(a , b)