from Project.controller.ProjectABC import ProjectABC

from Project.model.data_processor import DataProcessor
from Project.model.models import Finance

class FinanceController(ProjectABC):
    
    processor = DataProcessor()

    def __init__(self):
      pass

    
    def Add(self ,new_finace:Finance):       
        resalt=self.processor.create_finance(new_finace)
        return resalt
    
    def List(self):         
       resalt=self.processor.fetch_data('Finance')

     
       result = []
       for r in resalt:
           result.append((
              r.Finance_Id,
              r.Client_Id,
              r.Amount_granted,
              r.Exchange_date,
              r.Payment_term,
              r.Interest_rate,
             
        ))

       return result








       