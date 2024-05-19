class dad():
    def phone(self):
        print("dada phone")

class mom():
    def sweet(self):
        print("Mom sweet")

        
class son(dad,mom):
    def laptop(self):
        print("sons laptop")

ram = son()
ram.phone()
ram.sweet()
