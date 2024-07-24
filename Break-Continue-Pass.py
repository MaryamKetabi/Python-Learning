#Continue
Students = ['kevin' , 'jack' , 'peter' , 'bob' , 'sandie']

for S in Students:
    if S == 'peter':
        continue
    print(S + "\n")


#Break
students = ['kevin' , 'jack' , 'peter' , 'bob' , 'sandie']

for s in students:
    if s == 'peter':
        break
    print(s)

#Pass
Students = ['kevin' , 'jack' , 'peter' , 'bob' , 'sandie']

for S in Students:
    pass   