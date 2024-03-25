class Customer:
    def __init__(self, customer_id='', first_name='', last_name='', email='', phone='', address=''):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
    
    # Getter methods
    def get_customer_id(self):
        return self.customer_id
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_address(self):
        return self.address
    
    # Setter methods
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
    
    def set_first_name(self, first_name):
        self.first_name = first_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def set_email(self, email):
        self.email = email
    
    def set_phone(self, phone):
        self.phone = phone
    
    def set_address(self, address):
        self.address = address
    
    def print_info(self):
        print("Customer ID:", self.customer_id)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Phone:", self.phone)
        print("Address:", self.address)


class Account:
    def __init__(self, account_number='', account_type='', account_balance=0.0):
        self.account_number = account_number
        self.account_type = account_type
        self.account_balance = account_balance
    
    # Getter methods
    def get_account_number(self):
        return self.account_number
    
    def get_account_type(self):
        return self.account_type
    
    def get_account_balance(self):
        return self.account_balance
    
    # Setter methods
    def set_account_number(self, account_number):
        self.account_number = account_number
    
    def set_account_type(self, account_type):
        self.account_type = account_type
    
    def set_account_balance(self, account_balance):
        self.account_balance = account_balance
    
    def print_info(self):
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Account Balance:", self.account_balance)
    
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print("Deposit of $", amount, "successful.")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                print("Withdrawal of $", amount, "successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")
    
    def calculate_interest(self):
        interest_rate = 4.5  # Fixed interest rate
        interest_amount = (self.account_balance * interest_rate) / 100
        self.account_balance += interest_amount
        print("Interest calculated and added. New balance: $", self.account_balance)


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}
        self.next_customer_id = 1
        self.next_account_number = 100
    
    def create_customer(self):
        customer_id = str(self.next_customer_id)
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email address: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        customer = Customer(customer_id, first_name, last_name, email, phone, address)
        self.customers[customer_id] = customer
        self.next_customer_id += 1
        return customer
    
    def create_account(self, customer):
        account_number =str(self.next_account_number)
        account_type = input("Enter account type (e.g., Savings, Current): ")
        account_balance = float(input("Enter opening balance: $"))
        account = Account(account_number, account_type, account_balance)
        self.accounts[account_number] = account
        self.next_account_number += 1
        return account
    
    def main(self):
        while True:
            print("\nBanking Menu:")
            print("1. Create Customer")
            print("2. Create Account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Calculate Interest")
            print("6. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                customer = self.create_customer()
                print("\nCustomer created successfully. Customer ID:", customer.get_customer_id())
                customer.print_info()
            elif choice == '2':
                customer_id = input("Enter customer ID: ")
                if customer_id in self.customers:
                    customer = self.customers[customer_id]
                    account = self.create_account(customer)
                    print("\nAccount created successfully. Account Number:", account.get_account_number())
                    account.print_info()
                else:
                    print("Invalid customer ID.")
            elif choice == '3':
                account_number = input("Enter account number: ")
                if account_number in self.accounts:
                    amount = float(input("Enter deposit amount: $"))
                    self.accounts[account_number].deposit(amount)
                else:
                    print("Invalid account number.")
            elif choice == '4':
                account_number = input("Enter account number: ")
                if account_number in self.accounts:
                    amount = float(input("Enter withdrawal amount: $"))
                    self.accounts[account_number].withdraw(amount)
                else:
                    print("Invalid account number.")
            elif choice == '5':
                account_number = input("Enter account number: ")
                if account_number in self.accounts:
                    self.accounts[account_number].calculate_interest()
                else:
                    print("Invalid account number.")
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

bank = Bank()
bank.main()