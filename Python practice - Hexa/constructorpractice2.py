class teacher:
    def __init__(self,name,regno):
        self.name = name
        self.regno = regno
    def display(self):
        print("Name",self.name)
        print("Regno",self.regno)


t1=teacher("swe","123")
t2=teacher("adafd","123")



t1.display()
t2.display()
