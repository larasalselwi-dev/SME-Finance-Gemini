from Project.controller.ProjectABC import ProjectABC

from Project.model.data_processor import DataProcessor
from Project.model.data_processor import Guarantee

class GuaranteeControler(ProjectABC):
    
    processor = DataProcessor()

    def __init__(self):
      pass

    
    def Add(self ,new_guarantee:Guarantee):
       resalt= self.processor.create_Guarantee(new_guarantee)
       return resalt 
    
    def List(self):        
       resalt=self.processor.fetch_data('Guarante')


       result = []
       for r in resalt:
           result.append((
              r.Guarante_Id,
              r.Client_Id,
              r.Guarante_Type ,
              r.Guarante_state ,
              r.Guarante_amount 
     
        ))

       return result





       