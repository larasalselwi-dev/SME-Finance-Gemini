# models.py file
from datetime import date
from typing import Optional



class Client:

    def __init__(self, Full_name: str, ID_Card: int, Address:str,Phone_number:str,Email:str,
                 Gender:str,Marital_status:str,Job:str,Credit_rating:str ,Aage:int,Salary:float, 
                 Client_Id: Optional[int] = None):
       
        self.Client_Id = Client_Id 
     
        self.Full_name = Full_name
        self.ID_Card = ID_Card
        self.Address = Address
        self.Phone_number = Phone_number
        self.Email = Email
        self.Gender = Gender
        self.Marital_status = Marital_status
        self.Job = Job
        self.Aage = Aage
        self.Salary = Salary
        #التصنيف الائتماني
        self.Credit_rating=Credit_rating


class Request:
    def __init__(self, Client_Id: int,Finance_Type :str,Required_amount:int, Request_date: date, Request_State: str,Comments:str,
                  Request_Id: Optional[int] = None):
        self.Request_Id = Request_Id
        self.Client_Id = Client_Id
        self.Finance_Type = Finance_Type
        self.Required_amount = Required_amount
        self.Request_State = Request_State
        self.Request_date = Request_date
        self.Comments = Comments

class Finance:
    def __init__(self, Amount_granted: int, Exchange_date: date, Payment_term: str,Interest_rate:int,Client_Id:int, Finance_Id: Optional[int] = None):
        self.Finance_Id = Finance_Id
        self.Amount_granted = Amount_granted
        self.Exchange_date = Exchange_date
        self.Payment_term = Payment_term
        self.Interest_rate = Interest_rate
        self.Client_Id = Client_Id
        

class Guarantee:
    def __init__(self, Client_Id: int, Guarante_Type: str, Guarante_amount: int,Guarante_state:str, Guarante_Id: Optional[int] = None):
        self.Guarante_Id = Guarante_Id
        self.Client_Id = Client_Id
        self.Guarante_Type = Guarante_Type
        self.Guarante_state = Guarante_state
        
        self.Guarante_amount = Guarante_amount

