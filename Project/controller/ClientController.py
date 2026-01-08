from Project.controller.ProjectABC import ProjectABC

from Project.model.data_processor import DataProcessor
from Project.model.models import Client

class ClientController(ProjectABC):
    
    processor = DataProcessor()

    def __init__(self):
      pass

    
    def Add(self ,new_client:Client):
       resalt= self.processor.create_client(new_client)
       return resalt 
    
    def GetClient(self,client_id:int):        
       resalt=self.processor.get_client_by_id(client_id)     
       return resalt

    def List(self):        
       resalt=self.processor.fetch_data('Client')
  

       result = []
       for r in resalt:
           result.append((
              r.Client_Id,
              r.Full_name,
              r.Phone_number,
              r.Gender,
              r.Aage,
              r.ID_Card,
              r.Email,
              r.Marital_status,
              r.Job,
              r.Salary,
              r.Credit_rating,
              r.Address
        ))

       return result




       