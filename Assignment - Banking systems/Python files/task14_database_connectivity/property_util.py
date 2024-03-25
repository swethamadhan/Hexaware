
class PropertyUtil:
    @staticmethod
    def getPropertyString():
        server_name = "DESKTOP-GM6QDGG\\SQLEXPRESS"
        database_name = "HMBank"
        trusted_connection = "yes"
        return f"Driver={{SQL Server}};Server={server_name};Database={database_name};Trusted_Connection={trusted_connection};"
