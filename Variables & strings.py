a = 20 #int #temporary
b = 1.4 #float
print(type(a + b))
print(round(b))

###########################

c = "are you a robot?"  #double quotes
d = 'No! I\'m not.' #single quotes #\ escape the next one
e = "how old are you?\nI'm ten."
print(c)
print(d)
print(e)

###########################

print(9 // 2.5)
print(9 * 2.5)
print(9 ** 2.5)

###########################

alphabet = ('abcdefghijklm'
        'nopqrstuvwxyz')

print(len(alphabet))

f = alphabet[0:2]  #count= 2-0 = 2 , point= the last letter won't be stand
g = alphabet[1:2]  
h = alphabet[2]    
i = alphabet[:2]  
j = alphabet[2:]
k = alphabet[-2:-1]
l = alphabet[-9:-6]   
m = alphabet[9:18:2]

print("alphabet[0:2]:" , f)    
print("alphabet[1:2]:" , g)
print("alphabet[2]:" , h)
print("alphabet[:2]:" , i)
print("alphabet[2:]:" , j)
print("alphabet[-2:-1]:" , k)
print("alphabet[-9:-6]:" , l)
print("alphabet[9:18:2]:" , m)