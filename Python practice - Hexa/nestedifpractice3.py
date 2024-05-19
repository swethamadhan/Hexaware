s1=int(input("enter mark of s1: "))
s2=int(input("enter mark of s2: "))
s3=int(input("enter mark of s3: "))
s4=int(input("enter mark of s4: "))
s5=int(input("enter mark of s5: "))

subject = s1+s2+s3+s4+s5

print("Overall score: ",subject)

average = subject/5

print("Average: ",average)

if average < 35 :
    print("Additional class is required")
else:
    print("You are good to go")
          
