from Project.controller.ProjectABC import ProjectABC

from Project.model.data_processor import DataProcessor
from Project.model.data_processor import Request

class RequestController(ProjectABC):
    
    processor = DataProcessor()

    def __init__(self):
      pass

    
    def Add(self ,new_request:Request):
        
        resalt=self.processor.create_request(new_request)
        return resalt
    def List(self):   
       
       resalt=self.processor.fetch_data('Request')
   
       result = []
       for r in resalt:
           result.append((
              r.Request_Id,
              r.Client_Id,
              r.Finance_Type,
              r.Required_amount,
              r.Request_State,
              r.Request_date,
              r.Comments,
          
        ))

       return result





       