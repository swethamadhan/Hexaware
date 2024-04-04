import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc

class PropertyUtil:
    @staticmethod
    def getPropertyString():
        server_name = "DESKTOP-GM6QDGG\\SQLEXPRESS"
        database_name = "Virtual_Art_Gallery"
        trusted_connection = "yes"
        return f"Driver={{SQL Server}};Server={server_name};Database={database_name};Trusted_Connection={trusted_connection};"

