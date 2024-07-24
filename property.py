class Person:
    def __init__(self, Fname , Lname):
        self.Fname = Fname
        self.Lname = Lname
        self.email = f"the email addrs is: {self.Fname}.{self.Lname}@gmail.com"

    def fullname(self):
        return f'{self.Fname} {self.Lname}'
    
a = Person('Maryam' , 'Ketabi')
print(a.Fname)    
print(a.Lname)
print(a.email)
print(a.fullname() , "\n")

##################################################

class Person:
    def __init__(self, Fname , Lname):
        self.Fname = Fname
        self.Lname = Lname

    def fullname(self):
        return f'{self.Fname} {self.Lname}'
    
    def email(self):
        return f"the email addrs is: {self.Fname}.{self.Lname}@gmail.com"
    
a = Person('Maryam' , 'Ketabi')
print(a.Fname)    
print(a.Lname)
print(a.email())
print(a.fullname() , "\n")

####################################################

class Person:
    def __init__(self, Fname , Lname):
        self.Fname = Fname
        self.Lname = Lname

    @property                   #in line 54 we don't need ()
    def fullname(self):
        return f'{self.Fname} {self.Lname}'
    
    @property                   #in line 53 we don't need ()
    def email(self):
        return f"the email addrs is: {self.Fname}.{self.Lname}@gmail.com"
    
a = Person('Maryam' , 'Ketabi')
print(a.Fname)    
print(a.Lname)
print(a.email)
print(a.fullname , "\n")