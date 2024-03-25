from account import Account

class CurrentAccount(Account):
    def __init__(self, customer, balance, overdraft_limit):
        super().__init__(customer, "Current", balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds or exceeding overdraft limit")
            return False