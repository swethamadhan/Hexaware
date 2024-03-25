
import pyodbc
import property_util

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                connection_string = property_util.PropertyUtil.getPropertyString()
                DBConnection.connection = pyodbc.connect(connection_string)
                print("Connected Successfully")
            except pyodbc.Error as e:
                print(f"Connection failed: {e}")
        else:
            print("Connection already established")

        return DBConnection.connection  # Return the connection object

if __name__ == "__main__":
    conn = DBConnection.get_connection()
    if conn:
        conn.close()  # Close the connection if it was successfully established
