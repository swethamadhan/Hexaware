num_customers = int(input("Enter the number of customers: "))

for i in range(num_customers):
    initial_balance = float(input("Enter initial balance for customer {}: ".format(i+1)))
    annual_interest_rate = float(input("Enter annual interest rate for customer {} (%): ".format(i+1)))
    years = int(input("Enter number of years for customer {}: ".format(i+1)))
    
    future_balance = initial_balance * (1 + annual_interest_rate/100)**years
    print("Future balance for customer {} after {} years: ${:.2f}".format(i+1, years, future_balance))
