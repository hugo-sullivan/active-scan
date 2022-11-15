from abc import ABC, abstractmethod

class ScannerForm(ABC):
    def __init__(self, target, parameters):
        self.target = target
        self.parameters = parameters

    @abstractmethod
    def get(self):
        
        pass