import pyodbc
from propertyutil import PropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            try:
                connection_string = PropertyUtil.getPropertyString()
                DBConnection.connection = pyodbc.connect(connection_string)
                print("Connected Successfully")
            except pyodbc.Error as e:
                print(f"Connection failed: {e}")
        else:
            print("Connection already established")

if __name__ == "__main__":
    DBConnection.getConnection()
