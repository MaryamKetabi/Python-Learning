names = [] #mutable

print(names)
print(type(names))

names2 = ['maryam' , 'sara' , 'atena']
print(names2[:])

names2.append('parya') #add
print(names2[:])

names2[2:4] = [] #remove
print(names2[:])

print(names2[:-1])
print(names2[1:3])

names3 = ['mahdi' , 'amir' , 'sajad']
names3[2:] = ['arshia' , 'arman'] #add

print(names2 + names3)


