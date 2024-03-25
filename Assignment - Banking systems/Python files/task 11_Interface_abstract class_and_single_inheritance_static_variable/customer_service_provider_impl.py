from i_customer_service_provider import ICustomerServiceProvider

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].balance
        else:
            print("Account not found")
            return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount
            return self.accounts[account_number].balance
        else:
            print("Account not found")
            return None

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        else:
            print("Account not found")
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            if self.withdraw(from_account_number, amount):
                self.deposit(to_account_number, amount)
                return True
        else:
            print("Account not found")
            return False

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            return f"Account Number: {acc.acc_no}, Type: {acc.acc_type}, Balance: {acc.balance}, Customer: {acc.customer.name}"
        else:
            print("Account not found")
            return None