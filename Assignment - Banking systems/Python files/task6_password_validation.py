def display_transaction_history(transaction_history):
    print("Transaction History:")
    for transaction in transaction_history:
        print(transaction)

def main():
    transaction_history = []

    while True:
        transaction_type = input("Enter transaction type (deposit/withdrawal) or 'exit' to quit: ").lower()
        
        if transaction_type == 'exit':
            break
        elif transaction_type == 'deposit' or transaction_type == 'withdrawal':
            amount = float(input(f"Enter {transaction_type} amount: $"))
            transaction_history.append((transaction_type.capitalize(), amount))
        else:
            print("Invalid transaction type. Please enter 'deposit', 'withdrawal', or 'exit'.")

    display_transaction_history(transaction_history)

if __name__ == "__main__":
    main()
