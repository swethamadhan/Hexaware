from bank_service_provider_impl import BankServiceProviderImpl
from customer import Customer

class BankApp:
    def __init__(self):
        self.bank_service = BankServiceProviderImpl()

    def menu(self):
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Get Account Details")
        print("6. List Accounts")
        print("7. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter customer name: ")
                address = input("Enter customer address: ")
                acc_type = input("Enter account type (Savings/Current/Zero): ")
                balance = float(input("Enter initial balance: "))
                customer = Customer(name, address)
                acc_no = self.bank_service.create_account(customer, acc_type, balance)
                print(f"Account created successfully with Account Number: {acc_no}")
            elif choice == "2":
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                balance = self.bank_service.deposit(acc_no, amount)
                if balance is not None:
                    print(f"Deposit successful. Current Balance: {balance}")
            elif choice == "3":
                acc_no = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))
                success = self.bank_service.withdraw(acc_no, amount)
                if success:
                    print("Withdrawal successful")
            elif choice == "4":
                from_acc = int(input("Enter source account number: "))
                to_acc = int(input("Enter destination account number: "))
                amount = float(input("Enter transfer amount: "))
                success = self.bank_service.transfer(from_acc, to_acc, amount)
                if success:
                    print("Transfer successful")
            elif choice == "5":
                acc_no = int(input("Enter account number: "))
                details = self.bank_service.get_account_details(acc_no)
                if details is not None:
                    print(details)
            elif choice == "6":
                accounts = self.bank_service.list_accounts()
                for acc in accounts:
                    print(f"Account Number: {acc.acc_no}, Type: {acc.acc_type}, Balance: {acc.balance}, Customer: {acc.customer.name}")
            elif choice == "7":
                print("Exiting...")
                break

if __name__ == "__main__":
    app = BankApp()
    app.run()
