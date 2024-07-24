name = 'Jack'
age = 26

print('{} is {} years old.' .format(name , age))
print('{} is {} years old.' .format('amir' , 12) , "\n")
print('{0} is {1} years old.' .format(name , age))
print('{1} is {0} years old.' .format(name , age) , "\n")
print('{n} is {a} years old.' .format(n=name , a=age))
print('{a} is {n} years old.' .format(n=name , a=age) , "\n")
##########################################################
#dictionary

info = {'name':'Sara' , 'age':22} #index=0
info2 = {'name':'Mary' , 'age':21} #index=1

print('{0[name]} is {0[age]} years old and {1[name]} is {1[age]} years old and ' .format(info , info2) , "\n")
