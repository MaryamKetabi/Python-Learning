# print 'Hello' #SyntaxError
#print(1/0) #IndentationError
#print(1 + 2 - '3')  #type error
#f = open("test.txt") #filenotfound
#print(str.upper(23)) #type error

#############################################

# try:
#     print(str.upper(23))
# except TypeError:
#     print("your name must be string")

#############################################

try:
    f = open("test.txt")
    print(str.upper(23))
except FileNotFoundError:
    print("File does'nt exist!")    
except TypeError:
    print("your name must be string")

##############################################

try:
    f = open("test.txt")
    print(str.upper(23))
except IndentationError:
    print("File does'nt exist!")    
except TypeError:
    print("your name must be string")
else:
    print("This file workrd correctly")  

##############################################     

try:
    f = open("test.txt")
    print(str.upper(23))
except IndentationError:
    print("File does'nt exist!")    
except TypeError:
    print("your name must be string")
else:
    print("This file workrd correctly")  
finally:
    print("I don't care!")    
    
##############################################

try:
    f = open("test.txt")
    print(str.upper(23))
except Exception:
    print("File does'nt exist!")    
except TypeError:
    print("your name must be string")
else:
    print("This file workrd correctly")  
finally:
    print("I don't care!")   

