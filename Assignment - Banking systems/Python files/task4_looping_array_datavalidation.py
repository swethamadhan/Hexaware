import pyodbc

connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-GM6QDGG\SQLEXPRESS;'
                      'Database=HMBank;'
                      'Trusted_Connection=yes;')

cursor = connection.cursor()

def get_account_balance(account_number):
    query = "SELECT Balance FROM Accounts WHERE account_id = ?"
    cursor.execute(query, account_number)
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        return None

while True:
    account_number = input("Enter your account number: ")

    balance = get_account_balance(account_number)

    if balance is not None:
        print("Your account balance is: ", balance)
        break
    else:
        print("Invalid account number")

cursor.close()
connection.close()
