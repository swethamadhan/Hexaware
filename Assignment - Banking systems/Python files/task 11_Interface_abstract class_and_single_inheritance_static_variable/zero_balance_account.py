from account import Account

class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__(customer, "Zero Balance", 0)