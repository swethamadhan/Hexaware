class laptop:
    def __init__(self):
        self.ram=""
        
        self.processor=""
    def display(self):
        print("ram",self.ram)
        print("pro",self.processor)

hp=laptop()
hp.ram="8gb"
hp.processor="i5"
hp.price=50000


hp.display()
