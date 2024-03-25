from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number='', customer_name='', balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
    
    def get_account_number(self):
        return self.account_number
    
    def set_account_number(self, account_number):
        self.account_number = account_number
    
    def get_customer_name(self):
        return self.customer_name
    
    def set_customer_name(self, customer_name):
        self.customer_name = customer_name
    
    def get_balance(self):
        return self.balance
    
    def set_balance(self, balance):
        self.balance = balance
    
    def print_info(self):
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Balance:", self.balance)
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, account_number='', customer_name='', balance=0.0, interest_rate=0.0):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "successful. New balance:", self.balance)
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal of", amount, "successful. New balance:", self.balance)
        else:
            print("Insufficient balance.")
    
    def calculate_interest(self):
        interest_amount = self.balance * self.interest_rate / 100
        self.balance += interest_amount
        print("Interest calculated and added. New balance:", self.balance)


class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 1000
    
    def __init__(self, account_number='', customer_name='', balance=0.0):
        super().__init__(account_number, customer_name, balance)
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "successful. New balance:", self.balance)
    
    def withdraw(self, amount):
        if self.balance + self.OVERDRAFT_LIMIT >= amount:
            self.balance -= amount
            print("Withdrawal of", amount, "successful. New balance:", self.balance)
        else:
            print("Withdrawal amount exceeds available balance and overdraft limit.")
    
    def calculate_interest(self):
        print("Interest calculation not applicable for current account.")


class Bank:
    def create_account(self):
        print("Choose account type:")
        print("1. Savings Account")
        print("2. Current Account")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            account_number = input("Enter account number: ")
            customer_name = input("Enter customer name: ")
            initial_balance = float(input("Enter initial balance: "))
            interest_rate = float(input("Enter interest rate: "))
            return SavingsAccount(account_number, customer_name, initial_balance, interest_rate)
        elif choice == '2':
            account_number = input("Enter account number: ")
            customer_name = input("Enter customer name: ")
            initial_balance = float(input("Enter initial balance: "))
            return CurrentAccount(account_number, customer_name, initial_balance)
        else:
            print("Invalid choice.")
            return None
    
    def operate_account(self, account):
        while True:
            print("\nAccount Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Calculate Interest")
            print("4. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == '3':
                account.calculate_interest()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


# Main method
if __name__ == "__main__":
    bank = Bank()
    account = bank.create_account()
    if account:
        bank.operate_account(account)
