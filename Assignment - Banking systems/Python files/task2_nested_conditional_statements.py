#Task 2: Nested Conditional Statements
#Create a program that simulates an ATM transaction. Display options such as "Check Balance," 
#"Withdraw," "Deposit,". Ask the user to enter their current balance and the amount they want to 
#withdraw or deposit. Implement checks to ensure that the withdrawal amount is not greater than the 
#available balance and that the withdrawal amount is in multiples of 100 or 500. Display appropriate 
#messages for success or failure.



def check_balance(balance):
    print("Your current balance is: $", balance)

def withdraw(balance, amount):
    if amount > balance:
        print("Error: Insufficient funds.")
    elif amount % 100 != 0 and amount % 500 != 0:
        print("Error: Withdrawal amount must be in multiples of 100 or 500.")
    else:
        balance -= amount
        print("Withdrawal successful. Remaining balance is: $", balance)

def deposit(balance, amount):
    balance += amount
    print("Deposit successful. Current balance is: $", balance)

def main():
    balance = float(input("Enter your current balance: $"))

    print("\nOptions:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    option = int(input("Enter option (1/2/3): "))

    if option == 1:
        check_balance(balance)
    elif option == 2:
        amount = float(input("Enter withdrawal amount: $"))
        withdraw(balance, amount)
    elif option == 3:
        amount = float(input("Enter deposit amount: $"))
        deposit(balance, amount)
    else:
        print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
