#key:value pair, mutable

ages = {'maryam': 22, 'M.Hossein': 17, 'M.Hasan': 10}
print(ages , "\n") 
###########################

ages['Morteza'] = 50
ages['Somaye'] = 40
print(ages , "\n")
###########################

ages['Morteza','Somaye'] = 40 , 50
print(ages , "\n")
###########################

del ages['maryam']
print(ages , "\n")
###########################

ages['BlueMary'] = 22
print(ages , "\n")
###########################

print('Maryam' in ages)
print('M.Hasan' in ages , "\n")
###########################

print(ages.items() , "\n")
###########################

for i in ages.items():
    print(i , "\n")
###########################

for k, v in ages.items():
    print(k, v)