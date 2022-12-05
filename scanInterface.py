from abc import ABC, abstractmethod

class ScannerForm(ABC):
    def __init__(self, scan):
        self.scan = scan

    @abstractmethod
    def get(self):
        
        pass