#functions

def show(name): #arguman
    print('Hello ' + name) 

Name = input('What Is Your Name?\n')
show(Name) #parameter

########################################

def show(name): #arguman
    print('Hello ' + name) 

show('Maryam') #parameter

########################################

def show(name='Ali'): #arguman
    print('Hello ' + name) 

show() #parameter

########################################

def show(name='Ali'): #arguman
    print('Hello ' + name) 

show('Sarah') #parameter

########################################

#def show(name='Ali' , age): #arguman
    #print('Hello ' + name)
    #print('You are ' + age) #parameter without a default follows parameter with a default

#Age = int(input('How old are you?'))
#show('Sarah' , Age) #parameter