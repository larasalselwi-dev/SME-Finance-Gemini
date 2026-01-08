
import pyodbc

class DatabaseManager:
    """
    Manages connections to a SQL Server LocalDB instance using Windows Authentication.
    """
    def __init__(self):
        self.server = '(localdb)\\MSSQLLocalDB'
        self.database = 'Project_Financing_DB'
        # Use the correct driver name found on your system
        self.driver = '{ODBC Driver 17 for SQL Server}' 
        self.conn = None
        self.cursor = None
        self._connection_string = (
            f'DRIVER={self.driver};'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            f'Trusted_Connection=yes;'
        )

    def connect(self):
        """Establishes the database connection."""
        try:
            self.conn = pyodbc.connect(self._connection_string)
            self.cursor = self.conn.cursor()
            print(f"Connected to {self.database} successfully.")
            return self.cursor
        except pyodbc.Error as ex:
            print(f"Connection failed: {ex}")
            return None

    def close(self):
        """Closes the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Connection closed.")

