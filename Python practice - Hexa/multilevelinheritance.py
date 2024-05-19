class grandpa():
    def phone(self):
        print("grandpa phone")

class dad(grandpa):
    def money(self):
        print("dada money")

      
class son(dad):
    def laptop(self):
        print("sons laptop")

ram = son()
dada = dad()
dada.phone()
ram.money()
