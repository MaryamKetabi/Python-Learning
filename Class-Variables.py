#Variables: 1.instance 2.class

class Car2:
    wheel = 4 #class variable
    def __init__(self, n, p): 
        self.name = n
        self.price = p

    def show2(self):
        print(f"{self.name} has {self.wheel} wheels")

a = Car2('pride' , 100)   #pride and 100 are instance variables     
b = Car2('benz' , 900)

a.show2()        
b.show2()

####################################################################

class Car2:
    wheel = 4
    def __init__(self, n, p): 
        self.name = n
        self.price = p

    def show2(self):
        print(f"{self.name} has {Car2.wheel} wheels")

a = Car2('pride' , 100)        
b = Car2('benz' , 900)

a.show2()        
b.show2()

#####################################################################

class Car2:
    obj_name = 0 #numbers of objects
    
    def __init__(self, n, p): 
        self.name = n
        self.price = p
        
        Car2.obj_name += 1 #increase numbers of objects

a = Car2('pride' , 100)        
b = Car2('benz' , 900)

print(Car2.obj_name)