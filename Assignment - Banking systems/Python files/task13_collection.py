from collections import defaultdict
from typing import List, Set
class Account:
    def __init__(self, initial_balance: float, account_number: int):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance
        self.account_number = account_number
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise ValueError("Insufficient funds in your account.")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance}")
    def transfer(self, amount: float, recipient: 'Account'):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if self.balance < amount:
            raise ValueError("Insufficient funds in your account.")
        if recipient is None:
            raise ValueError("Invalid recipient account.")
        self.balance -= amount
        recipient.balance += amount
        print(f"Transfer successful. New balance: ${self.balance}")
    def get_balance(self) -> float:
        return self.balance
    def get_account_number(self) -> int:
        return self.account_number
class HMBank:
    def __init__(self):
        self.accounts_list: List[Account] = []
        self.accounts_set: Set[Account] = set()
        self.accounts_map = defaultdict(Account)  
    def add_account(self, account: Account):
        self.accounts_list.append(account)
        self.accounts_set.add(account)
        self.accounts_map[account.get_account_number()] = account
    def withdraw(self, account_number: int, amount: float):
        account = self.accounts_map.get(account_number)
        if account is None:
            raise ValueError("Account not found.")
        account.withdraw(amount)
    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        from_account = self.accounts_map.get(from_account_number)
        to_account = self.accounts_map.get(to_account_number)
        if from_account is None or to_account is None:
            raise ValueError("Invalid account(s).")
        from_account.transfer(amount, to_account)
    def list_accounts(self):
        sorted_accounts = sorted(self.accounts_list, key=lambda acc: acc.get_account_number())
        for account in sorted_accounts:
            print(f"Account Number: {account.get_account_number()}, Balance: {account.get_balance()}")
def main():
    try:
        bank = HMBank()
        account1 = Account(1000, 11111111)
        account2 = Account(500, 22222222)
        bank.add_account(account1)
        bank.add_account(account2)
        print("Listing accounts before transactions:")
        bank.list_accounts()
        print("\nPerforming transactions:")
        bank.withdraw(11111111, 200)
        bank.transfer(11111111, 22222222, 100)
        print("\nListing accounts after transactions:")
        bank.list_accounts()
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
