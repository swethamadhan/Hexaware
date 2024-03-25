from dbconnection import DBConnection

class BankServiceProviderImpl:
    @staticmethod
    def create_account(account):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Accounts (account_id, customer_id, account_type, balance) VALUES (?, ?, ?, ?)",
                           (account.account_number, account.customer_name, account.account_type, account.balance))
            conn.commit()
            print("Account created successfully!")
        except Exception as e:
            print("Error:", e)
        finally:
            if conn:
                conn.close()

    # Other methods remain unchanged




    @staticmethod
    def deposit(acc_number, amount):
        conn = None
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Accounts SET Balance = balance + ? WHERE account_id = ?", (amount, acc_number))
            conn.commit()
            print("Deposit successful!")
        except Exception as e:
            print("Error:", e)
        finally:
            if conn:
                conn.close()

    @staticmethod
    def withdraw(acc_number, amount):
        conn = None
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Accounts SET Balance = balance - ? WHERE account_id = ?", (amount, acc_number))
            conn.commit()
            print("Withdrawal successful!")
        except Exception as e:
            print("Error:", e)
        finally:
            if conn:
                conn.close()

    @staticmethod
    def transfer(from_account_number, to_account_number, amount):
        conn = None
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Accounts SET balance = balance - ? WHERE account_id = ?", (amount, from_account_number))
            cursor.execute("UPDATE Accounts SET balance = balance + ? WHERE account_id = ?", (amount, to_account_number))
            conn.commit()
            print("Transfer successful!")
        except Exception as e:
            print("Error:", e)
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_account_details(account_number):
        conn = None
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Accounts WHERE account_id = ?", (account_number,))
            row = cursor.fetchone()
            if row:
                print("Account Details:")
                print("Account Number:", row[0])
                print("Customer Name:", row[1])
                print("Account Type:", row[2])
                print("Balance:", row[3])
            else:
                print("Account not found!")
        except Exception as e:
            print("Error:", e)
        finally:
            if conn:
                conn.close()

    @staticmethod
    def list_accounts():
        conn = None
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Accounts")
            rows = cursor.fetchall()
            if rows:
                print("List of Accounts:")
                for row in rows:
                    print("Account Number:", row[0])
                    print("Customer Name:", row[1])
                    print("Account Type:", row[2])
                    print("Balance:", row[3])
                    print("-------------------------")
            else:
                print("No accounts found!")
        except Exception as e:
            print("Error:", e)
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_transactions(account_number, from_date, to_date):
        conn = None
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Transactions WHERE account_id = ? AND transaction_date BETWEEN ? AND ?",
                           (account_number, from_date, to_date))
            rows = cursor.fetchall()
            if rows:
                print("Transactions:")
                for row in rows:
                    print("Transaction ID:", row[0])
                    print("Account Number:", row[1])
                    print("Transaction Type:", row[2])
                    print("Amount:", row[3])
                    print("Transaction Date:", row[4])
                    print("-------------------------")
            else:
                print("No transactions found!")
        except Exception as e:
            print("Error:", e)
        finally:
            if conn:
                conn.close()
