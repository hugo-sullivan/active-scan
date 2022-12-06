from abc import ABC, abstractmethod

class ScannerForm(ABC):
    def __init__(self, scan_param):
        self.scan_param = scan_param

    @abstractmethod
    def scan(self):
        
        pass