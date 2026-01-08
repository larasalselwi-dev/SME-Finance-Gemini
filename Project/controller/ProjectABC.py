from abc import ABC,abstractmethod


class ProjectABC(ABC):
    @abstractmethod
    def Add(self):
        pass



    @abstractmethod
    def List(self):
        pass 