a=int(input("Enter a: "))
b=int(input("Enter b: "))

def printrange():
    print("Numbers from a:",a,"Numbers from b:",b)

printrange()



def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)

a=int(input("Enter a: "))
b=int(input("Enter b: "))
printrange(a,b)
