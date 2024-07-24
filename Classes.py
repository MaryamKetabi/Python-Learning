class Car: #blueprint
    pass

a = Car() #object / instancce
b = Car() 

a.name = 'pride' #atribute / property
b.name = 'benz'

a.price = 100 # . is dot notation
b.price = 900

print(a.price)
print(b.name , "\n")

print(f"{a.name} costs {a.price}")
print(f"{b.name} costs {b.price}")

