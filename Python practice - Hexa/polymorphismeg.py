class animal():
    def sound(self):
        print("Animal makes a sound")

#method overriding
class dog(animal):
    def sound(self):
        print("dog barks")

class bird(animal):
    def sound(self):
        print("Birds sing")

a1=animal()
a1.sound()

b1=bird()
b1.sound()
