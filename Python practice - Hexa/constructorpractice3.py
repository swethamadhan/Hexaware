class calculator:
    def __init__ (self,a,b):
        self.num1 = a
        self.num2 = b

    def add(self):
        print("add", self.num1+self.num2)

    def sub(self):
        print("sub", self.num1-self.num2)

    def mul(self):
        print("mul", self.num1*self.num2)

    def div(self):
        print("div", self.num1/self.num2)

user1 = calculator(10,2)

user1.add()

