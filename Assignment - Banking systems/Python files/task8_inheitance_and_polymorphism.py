class Account:
    def __init__(self, account_number='', account_type='', account_balance=0.0):
        self.account_number = account_number
        self.account_type = account_type
        self.account_balance = account_balance
    
    def deposit(self, amount):
        self.account_balance += amount
        print("Deposit of", amount, "successful. New balance:", self.account_balance)
    
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print("Withdrawal of", amount, "successful. New balance:", self.account_balance)
        else:
            print("Insufficient balance.")
    
    def calculate_interest(self):
        pass  # To be overridden by subclasses


class SavingsAccount(Account):
    def __init__(self, account_number='', account_balance=0.0, interest_rate=0.0):
        super().__init__(account_number, 'Savings', account_balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        interest_amount = self.account_balance * self.interest_rate / 100
        self.account_balance += interest_amount
        print("Interest calculated and added. New balance:", self.account_balance)


class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000  # Constant overdraft limit for all current accounts
    
    def __init__(self, account_number='', account_balance=0.0):
        super().__init__(account_number, 'Current', account_balance)
    
    def withdraw(self, amount):
        if self.account_balance + self.OVERDRAFT_LIMIT >= amount:
            self.account_balance -= amount
            print("Withdrawal of", amount, "successful. New balance:", self.account_balance)
        else:
            print("Withdrawal amount exceeds available balance and overdraft limit.")


class Bank:
    def create_account(self):
        print("Choose account type:")
        print("1. Savings Account")
        print("2. Current Account")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            interest_rate = float(input("Enter interest rate: "))
            return SavingsAccount(account_number, initial_balance, interest_rate)
        elif choice == '2':
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            return CurrentAccount(account_number, initial_balance)
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
                if isinstance(account, SavingsAccount):
                    account.calculate_interest()
                else:
                    print("Interest calculation not applicable for current account.")
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
