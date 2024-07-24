#class Car:
#    def show():
#c1 = Car() #این شی به متدهای کلاس دسترسی دارد

#c1.show() #در اینجا متد شاو هیچ آرگومانی دریافت نمی‌کند پس ارور میدهد
#در واقع خود C1 را برای show میفرستد ولی ما نمی‌بینیم

#راه حل:

class Car:
    def show(self):
        print('This is method.' , "\n")
        print(self , "\n")

c1 = Car() #این شی به متدهای کلاس دسترسی دارد

c1.show() #الان سی1 به طور اتوماتیک ارسال میشود به متد شو

print(c1 , "\n") #وقتی خود سی1 را هم چاپ میکنیم نتیجه یکسان با خط کد بالا دارد


#####################################################

class Car2:
    def __init__(self): #built in func
        print('This is intializer.')

    def show2(self):
        print('This is method.' , "\n")

a = Car2()        
b = Car2()

#a.name = 'pride' 
#b.name = 'benz'

#a.price = 100 
#b.price = 900

#####################################################

class Car2:
    def __init__(self, n, p): #built in func
        print('This is intializer.')
        self.name = n
        self.price = p

    def show2(self):
        print('This is method.' , "\n")

a = Car2('pride' , 100)        
b = Car2('benz' , 900)

print(f"{a.name} costs {a.price}")
print(f"{b.name} costs {b.price}")


#####################################################

class Car2:
    def __init__(self, n, p): #built in func
        print('This is intializer.')
        self.name = n
        self.price = p

    def show2(self):
        print(f"{self.name} costs {self.price}")

a = Car2('pride' , 100)        
b = Car2('benz' , 900)

a.show2()        
b.show2()