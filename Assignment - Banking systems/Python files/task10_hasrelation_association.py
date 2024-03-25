

import re

class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone_number=None, address=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return f"Customer ID: {self.customer_id}\n" \
               f"First Name: {self.first_name}\n" \
               f"Last Name: {self.last_name}\n" \
               f"Email: {self.email}\n" \
               f"Phone Number: {self.phone_number}\n" \
               f"Address: {self.address}"

    # Getter and setter methods for attributes
    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        if self.validate_email(email):
            self.email = email
        else:
            print("Invalid email format")

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        if self.validate_phone_number(phone_number):
            self.phone_number = phone_number
        else:
            print("Invalid phone number format")

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    # Method to validate email format
    def validate_email(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        else:
            return False

    # Method to validate phone number format
    def validate_phone_number(self, phone_number):
        if re.match(r"^\d{10}$", phone_number):
            return True
        else:
            return False


#2

class Account:
    # Class variable to keep track of the last account number used
    last_account_number = 1000

    def __init__(self, account_number=None, account_type=None, balance=0, customer=None):
        if account_number is None:
            # Automatically generate a unique account number if not provided
            Account.last_account_number += 1
            self.account_number = Account.last_account_number
        else:
            self.account_number = account_number

        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def __str__(self):
        return f"Account Number: {self.account_number}\n" \
               f"Account Type: {self.account_type}\n" \
               f"Balance: {self.balance}\n" \
               f"Customer: {self.customer}"

    # Getter and setter methods for attributes
    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("Deposit amount should be greater than zero.")
            return False

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Insufficient balance.")
            return False



#1 1
class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store account_number: account_object mapping

    def create_account(self, customer, accNo, accType, balance):
        # Check if account number already exists
        if accNo in self.accounts:
            print("Account number already exists.")
            return

        # Create a new account object
        new_account = Account(accNo, accType, balance, customer)
        
        # Add the account to the dictionary
        self.accounts[accNo] = new_account

        print(f"Account created successfully for {customer.get_first_name()} {customer.get_last_name()}.")

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_balance()
        else:
            print("Account number not found.")
            return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
            return self.accounts[account_number].get_balance()
        else:
            print("Account number not found.")
            return None

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        else:
            print("Account number not found.")
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            from_account = self.accounts[from_account_number]
            to_account = self.accounts[to_account_number]

            if from_account.get_balance() >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("One or both account numbers not found.")

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            customer = account.get_customer()
            print(f"Account Number: {account_number}")
            print("Customer Details:")
            print(customer)
            print(f"Account Type: {account.get_account_type()}")
            print(f"Balance: {account.get_balance()}")
        else:
            print("Account number not found.")


#2

class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store account_number: account_object mapping
        self.next_account_number = 1001  # Starting account number

    def create_account(self, customer, accType, balance):
        # Generate the next account number
        accNo = self.next_account_number
        self.next_account_number += 1  # Increment for the next account

        # Create a new account object
        new_account = Account(accNo, accType, balance, customer)

        # Add the account to the dictionary
        self.accounts[accNo] = new_account

        print(f"Account created successfully for {customer.get_first_name()} {customer.get_last_name()}.")

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_balance()
        else:
            print("Account not found.")
            return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
            return self.accounts[account_number].get_balance()
        else:
            print("Account not found.")
            return None

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
            return self.accounts[account_number].get_balance()
        else:
            print("Account not found.")
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            from_balance = self.accounts[from_account_number].get_balance()
            if from_balance >= amount:
                self.accounts[from_account_number].withdraw(amount)
                self.accounts[to_account_number].deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("One or both accounts not found.")

    def getAccountDetails(self, account_number):
        if account_number in self.accounts:
            print(self.accounts[account_number])
        else:
            print("Account not found.")

    # Other methods remain the same


#3

class BankApp:
    def __init__(self):
        self.bank = Bank()

    def display_menu(self):
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Get Balance")
        print("5. Transfer")
        print("6. Get Account Details")
        print("7. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account_menu()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.get_balance()
            elif choice == "5":
                self.transfer()
            elif choice == "6":
                self.get_account_details()
            elif choice == "7":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_account_menu(self):
        print("\nCreate Account Menu:")
        print("1. Savings Account")
        print("2. Current Account")
        acc_type = input("Enter account type (1 for Savings, 2 for Current): ")
        if acc_type == "1":
            acc_type = "Savings"
        elif acc_type == "2":
            acc_type = "Current"
        else:
            print("Invalid account type.")
            return

        customer_id = input("Enter Customer ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email Address: ")
        phone_number = input("Enter Phone Number: ")
        address = input("Enter Address: ")
        balance = float(input("Enter Initial Balance: "))

        customer = Customer(customer_id, first_name, last_name, email, phone_number, address)
        self.bank.create_account(customer, acc_type, balance)

    def deposit(self):
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Deposit Amount: "))
        new_balance = self.bank.deposit(account_number, amount)
        print(f"Deposit successful. New balance: {new_balance}")

    def withdraw(self):
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Withdrawal Amount: "))
        new_balance = self.bank.withdraw(account_number, amount)
        if new_balance is not None:
            print(f"Withdrawal successful. New balance: {new_balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        account_number = int(input("Enter Account Number: "))
        balance = self.bank.get_account_balance(account_number)
        print(f"Current balance: {balance}")

    def transfer(self):
        from_account_number = int(input("Enter From Account Number: "))
        to_account_number = int(input("Enter To Account Number: "))
        amount = float(input("Enter Transfer Amount: "))
        success = self.bank.transfer(from_account_number, to_account_number, amount)
        if success:
            print("Transfer successful.")
        else:
            print("Transfer failed.")

    def get_account_details(self):
        account_number = int(input("Enter Account Number: "))
        details = self.bank.getAccountDetails(account_number)
        if details:
            print("Account Details:")
            print(details)
        else:
            print("Account not found.")

if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.run()
