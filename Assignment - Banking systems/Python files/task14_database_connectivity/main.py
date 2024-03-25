
from bankserviceproviderimpl import BankServiceProviderImpl
from account import Account

def main():
    bank_service = BankServiceProviderImpl()

    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Get Account Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acc_number = int(input("Enter account number: "))
        name = input("Enter customer name: ")
        acc_type = input("Enter account type: ")
        balance = float(input("Enter balance: "))
        account = Account(acc_number, name, acc_type, balance)
        bank_service.create_account(account)
    elif choice == "2":
        acc_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        bank_service.deposit(acc_number, amount)
    elif choice == "3":
        acc_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        bank_service.withdraw(acc_number, amount)
    elif choice == "4":
        from_acc = int(input("Enter source account number: "))
        to_acc = int(input("Enter destination account number: "))
        amount = float(input("Enter transfer amount: "))
        bank_service.transfer(from_acc, to_acc, amount)
    elif choice == "5":
        acc_number = int(input("Enter account number: "))
        bank_service.get_account_details(acc_number)
    elif choice == "6":
        print("Exiting...")
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
