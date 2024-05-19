class dad:
    def money(self):
        print("dadas money")
        
class land:
    def important(self):
        print("important land")
        
class son1(dad, land):  
    pass

class son2(dad):
    pass

class son3(dad):
    pass


s1 = son1()


s1.money()      
s1.important()  
