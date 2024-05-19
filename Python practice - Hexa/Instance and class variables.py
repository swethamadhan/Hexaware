class phone():
    chargertype = "C-Type"

    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("ChargerType:",self.chargertype)

phone.chargertype = "B=Type"

samsung = phone("samsung","10000")
samsung.display()

redmi = phone("redmi","50000")
redmi.display()

oppo = phone("oppo","55000")
oppo.display()
