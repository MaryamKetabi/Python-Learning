#tuples are immutable

names = 'amir' , 'jack' , 'kevin' , (12 , 43 , 24) , ['anan' , 'bob' , ('brad' , 'sara')]

print(names , "\n")
######################
L = []
T = ()

print(type(L))
print(type(T) , "\n")

######################

L = [1]
T = (1)

print(type(L))
print(type(T), "\n")

######################

L = [1]
T = ('maryam')

print(type(L))
print(type(T), "\n")

######################

L = [1]
T = ('maryam' ,)

print(type(L))
print(type(T) , "\n")