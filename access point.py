#access-point: public , protected , private


class person:
    name = 'amir'    #public , no _
    _age = 32        #protected , one _
    __height = 180   #private , two __



class Male(person):
    pass

############################


class person:
    name = 'amir'    #everywhere
    _age = 32        #in children classes
    __height = 180   #only in the class



class Male(person):
    def show(self):
        print(self._age)

m = Male()        
m.show()

##############################

class person:
    name = 'amir'    
    _age = 32       
    __height = 180   



class Male(person):
    def show(self):
        print(self.__height)

P = person()
print(P._person__height) #name mangling
