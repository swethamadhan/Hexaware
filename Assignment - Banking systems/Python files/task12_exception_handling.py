class InsufficientFundsException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidAccountException(Exception):
    def __init__(self, message):
        super().__init__(message)

class OverDraftLimitExceededException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class NullPointerException(Exception):
    def __init__(self, message):
        super().__init__(message)

class HMBank:
    def __init__(self, initial_balance, account_number):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance
        self.account_number = account_number

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise InsufficientFundsException("Insufficient funds in your account.")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance}")

    def transfer(self, amount, recipient):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if self.balance < amount:
            raise InsufficientFundsException("Insufficient funds in your account.")

        if recipient.account_number != 12345678: 
            raise InvalidAccountException("Invalid recipient account number.")

        self.balance -= amount
        recipient.balance += amount
        print(f"Transfer successful. New balance: ${self.balance}")

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number


def main():
    try:
        account1 = HMBank(1000, 11111111)
        account2 = HMBank(500, 22222222) 
        print(f"Account 1 balance before withdrawal: ${account1.get_balance()}")
        account1.withdraw(1200)  
        print("Transferring from account 1 to account 2...")
        account1.transfer(200, None)  

        print(f"Account 1 balance after successful operations: ${account1.get_balance()}")
        print(f"Account 2 balance after successful operations: ${account2.get_balance()}")
    except InsufficientFundsException as e:
        print(f"Error: {e}")
    except InvalidAccountException as e:
        print(f"Error: {e}")
    except OverDraftLimitExceededException as e:
        print(f"Error: {e}")
    except NullPointerException as e:
        print("Error: Null reference encountered.")
    finally:
        pass


if __name__ == "__main__":
    main()
