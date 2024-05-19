a=int(input("Enter your score : "))
if(a<35):
    print("Poor student")
elif(a>35 and a<70):
    print("average student")
elif(a>=70 and a<100):
    print("Good student")
else:
    print("Invalid number")
