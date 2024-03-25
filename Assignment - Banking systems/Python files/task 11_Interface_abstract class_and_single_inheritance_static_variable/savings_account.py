from account import Account

class SavingsAccount(Account):
    def __init__(self, customer, balance):
        super().__init__(customer, "Savings", balance)