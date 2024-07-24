names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.append('Mahdi')

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.append(['Mahdi'])

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.extend('Mahdi')

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.extend(['Mahdi'])

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.extend(['Mahdi' , 'AliReza'])

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.insert(len(names) , 'Mahdi')

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.insert(2 , 'Mahdi')

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.remove('kevin')

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.remove('sara')

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.pop()

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.pop(3)

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.pop()

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.clear()

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

x = names.index('sara')

print(x)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

x = names.index('sara' , 0 , 4)

print(x)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

x = names.count('sara')

print(x)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.sort()

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

names.reverse()

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

del names[1:3]

print(names)
###############################################################
names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

del names[:]

print(names)
###############################################################
#names = ['kevin' , 'sara' , 'maral' , 'maryam' , 'sara']

#del names

#print(names)