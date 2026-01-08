# Assuming database_manager.py is in the same directory
from Project.model.database_manager import DatabaseManager


from Project.model.models import Client, Request, Finance, Guarantee
import pyodbc

class DataProcessor:
    # ... (Keep the __init__ and execute_query methods from the previous answer) ...
    def __init__(self):
        self.db_manager = DatabaseManager()

    def fetch_data(self, table_name):
        """Connects, fetches  rows, and closes the connection."""
        cursor = self.db_manager.connect()
        
        if cursor:
            try:
                # Be careful with table names in f-strings; use parameterization for values
                query = f"SELECT  * FROM {table_name}"
                cursor.execute(query)
                rows = cursor.fetchall()
                #print(f"\n--- Data from {table_name} ---")
                #for row in rows:
                 #   print(row)
               # print("--- End of Data ---\n")
                return rows
            except pyodbc.Error as ex:
                print(f"Error executing query: {ex}")
            finally:
                self.db_manager.close()
        else:
            print("Could not fetch data due to connection error.")

    # --- Specific Methods for Operations ---




    def execute_query(self, query, params=None, commit=False):
        # ... (Implementation of execute_query goes here) ...
        cursor = self.db_manager.connect()
        results = None
        if cursor:
            try:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                if commit:
                    self.db_manager.conn.commit()
                    # print("Query executed and committed successfully.")
                if not commit and cursor.description:
                    results = cursor.fetchall()
            except pyodbc.Error as ex:
                print(f"Error executing query: {ex}")
                if commit and self.db_manager.conn:
                    self.db_manager.conn.rollback() 
            finally:
                self.db_manager.close()
        return results

    # --- New Methods using Model Classes ---





    def get_client_by_id(self,client_id: int) :

        cursor = self.db_manager.connect()
        if not cursor: return False

        try:
            
          cursor.execute("SELECT * FROM Client WHERE Client_Id = ?", client_id)
          row = cursor.fetchone()
          return row
          

        except pyodbc.Error as ex:
            print(f"Transaction failed: {ex}")
            self.db_manager.conn.rollback()
            return False

        finally:
            self.db_manager.close() 

    def create_client(self, client_model: Client):
       
  
        cursor = self.db_manager.connect()
        if not cursor: return False

        try:
            
            # 1. Insert into Client table and get ID
            client_query = "INSERT INTO Client (Full_name , ID_Card , Address , Phone_number , Email , Gender , Marital_status , Job , Credit_rating , Aage ,Salary ) VALUES (?, ?,?,?,?,?,?,?,?,?,?); "
            cursor.execute(client_query, (client_model.Full_name, client_model.ID_Card,client_model.Address,
                                          client_model.Phone_number,client_model.Email,
                                          client_model.Gender,client_model.Marital_status,client_model.Job,
                                          client_model.Credit_rating , client_model.Aage, client_model.Salary))
            #client_model.client_id = cursor.fetchval()

            self.db_manager.conn.commit()
            
            #print(f"Successfully created a complete request ")
            return True

        except pyodbc.Error as ex:
            print(f"Transaction failed: {ex}")
            self.db_manager.conn.rollback()
            return False

        finally:
            self.db_manager.close()


    def create_request(self,  request_model: Request):
     
        cursor = self.db_manager.connect()
        if not cursor: return False

        try:
            # 2. Insert into Request table (using the new client_id)
            request_query = "INSERT INTO Request (Client_Id, Request_date, Request_State ,Finance_Type,Required_amount ,Comments) VALUES (?, ?, ?, ?, ?, ?); SELECT SCOPE_IDENTITY();"
            request_params = ( request_model.Client_Id,request_model.Request_date, request_model.Request_State,request_model.Finance_Type
                              ,request_model.Required_amount,request_model.Comments)
            cursor.execute(request_query, request_params)
           # request_model.request_id = cursor.fetchval()
    
            self.db_manager.conn.commit()
            
          #  print(f"Successfully created a complete request .")
            return True

        except pyodbc.Error as ex:
            print(f"Transaction failed: {ex}")
            self.db_manager.conn.rollback()
            return False

        finally:
            self.db_manager.close()
        
    def create_finance(self,  finance_model: Finance):
        
        cursor = self.db_manager.connect()
        if not cursor: return False

        try:     # 3. Insert into Finance table (using the new request_id)
            finance_query = "INSERT INTO Finance (Client_Id, Exchange_date, Amount_granted,Interest_rate,Payment_term) VALUES (?, ?, ?, ?, ?); SELECT SCOPE_IDENTITY();"
            finance_params = ( finance_model.Client_Id, finance_model.Exchange_date,finance_model.Amount_granted ,finance_model.Interest_rate
                             ,finance_model.Payment_term)
            cursor.execute(finance_query, finance_params)
            #finance_model.finance_id = cursor.fetchval()

            self.db_manager.conn.commit()
            
            print(f"Successfully created a complete request .")
            return True

        except pyodbc.Error as ex:
            print(f"Transaction failed: {ex}")
            self.db_manager.conn.rollback()
            return False

        finally:
            self.db_manager.close()

    def create_Guarantee(self,  guarantee_model: Guarantee):
     
        cursor = self.db_manager.connect()
        if not cursor: return False

        try:
            # 4. Insert into Guarantees table (using the new finance_id)
            guarantee_query = "INSERT INTO Guarante (Client_Id, Guarante_amount, Guarante_state,Guarante_Type) VALUES (?, ?, ?, ?);"
            guarantee_params = (guarantee_model.Client_Id, guarantee_model.Guarante_amount,guarantee_model.Guarante_state,guarantee_model.Guarante_Type)
            cursor.execute(guarantee_query, guarantee_params)
            
            self.db_manager.conn.commit()

            print(f"Successfully created a complete request ")
            return True

        except pyodbc.Error as ex:
            print(f"Transaction failed: {ex}")
            self.db_manager.conn.rollback()
            return False

        finally:
            self.db_manager.close()

# --- Usage Example ---

    
