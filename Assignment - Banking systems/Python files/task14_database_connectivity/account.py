class Account:
    def __init__(self, account_number, customer_name, account_type, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.account_type = account_type
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Customer Name: {self.customer_name}, Account Type: {self.account_type}, Balance: {self.balance}"
