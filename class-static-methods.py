#methods: 1.instance 2.class 3.statics

class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def show(self): #instance methods wich recieve instances
        print(f"{self.name} is {self.height}")


P1 = Person('Amir' , 179) 
P1.show()

################################################

import datetime

class Person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self): #instance methods wich recieve instances
        print(f"{self.name} is {self.height} and his age is {self.age}")

    @classmethod
    def birth(cls, name, height, age): #class methods wich recieve the classes
        return cls(name, height, datetime.datetime.now().year - age)

P1 = Person.birth('Amir' , 179 , 1990) 
P1.show()

################################################

import datetime

class Person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self): #instance methods wich recieve instances
        print(f"{self.name} is {self.height} and his age is {self.age}")

    @classmethod
    def birth(cls, name, height, age): #class methods wich recieve the classes
        return cls(name, height, datetime.datetime.now().year - age)
    
    @staticmethod
    def is_adult(age):
        if age > 18:
            print('Yes')
        else:
            print('No')


P1 = Person.birth('Amir' , 179 , 1990) 
P1.show()
Person.is_adult(98) #important