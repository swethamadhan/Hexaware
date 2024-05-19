salary = int(input("Enter your salary: "))
age = int(input("Enter your age: "))

if salary >= 20000 or age <= 25:
    loan = int(input("Enter your required loan amount: "))
    if loan <= 50000:
        print("You are eligible for the loan")
    else:
        print("Maximum loan amount is 50000")
else:
    print("Not eligible for loan")
