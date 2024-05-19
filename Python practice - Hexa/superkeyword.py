class a:
    def __init__(self):
        print("A")
    def display(self):
        print("a class")

class b:
    def __init__(self):
        print("B")
    def display(self):
        print("b class")

class c:
    def __init__(self):
        self.obj_a = a()
        self.obj_b = b()
        print("C")
    def display(self):
        print("C class")

ob1 = c()
