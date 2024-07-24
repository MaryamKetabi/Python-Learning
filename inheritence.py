class Car:
    wheel = 4
    def __init__(self, name):
        self.name = name


    def show(self):
        print(f"I have a {self.name}")

class Motor(Car): #we send a class fof Motor class
    wheel = 2
    #این کلاس به خطوط 3 تا 8 کلاس اول دسترسی دارد
    #مقدار wheel رو خودمون تغییر دادیم به 2
    def show(self):
        super().show() #اول تابع شو تابع پدر را نشان میدهد
        print(f"I ride a {self.name}")

#m = Motor('Honda')   
#m.show()
#print(m.wheel) #چون داخل کلاس خودم هست، دیگه نمیره اون کلاس رو بگرده
#help(m) #MRO= اگه یه متد یا اتربیوت داخل کلاس خودم نبود، کجا برم دنبالش بگردم

############################################################

class Car: #parent #superclass
    wheel = 4
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"I have a {self.name}")


class Motor(Car): #subclass #child
    wheel = 2
    def __init__(self, name, helmet):
        super().__init__(name) 
        self.helmet = helmet


m = Motor('Honda' , 'no') 
m.show()  
