#unordered, no duplicate elements, support maths opperands

names = {'amir' , 'sara' , 'kevin'}
print(names) #run it 4 times for example

############################

names = {'amir' , 'sara' , 'kevin' , 'amir'}
print(names) #run it 4 times for example

############################

names = {'amir' , 'sara' , 'kevin' , 'Amir'}
print(names) #run it 4 times for example

############################

nums = {1 , 2 , 3}
if 3 in nums:
    print("yes")

###########################

Nums = {1 , 2 , 3}
if 3 not in Nums:
    print("yes")

###########################

Numbers = {1 , 2 , 3}
if 21 in Numbers:
    print("yes")

###########################

basket = {}
print(basket)

###########################

basket = set()
print(basket)

###########################

basket = {'apple' , 'orange' , 'apple' , ' pear' , 'orange' , 'banana'}
print(basket)
#if orange in basket:
#   print("yes")

###########################

A = set('abcdefghijklm')
B = set('ghijklmniopqrstuv')

print(A)
print(A - B)
print(A | B)
print(A & B)
print(A ^ B)