a = 10 #in the root = global scope

def show():
    print(a)

show()

###################
#an error
# def show2():
#    b = 20 #local Scope

#show(b)
###################
a = 10 #in the root = global scope

def show():
    a = 20 #it's near and have proprioty. it's not that above a. it's another
    print(a)

show() 

