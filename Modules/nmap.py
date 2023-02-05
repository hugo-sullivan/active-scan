import nmap3
from scanInterface import ScannerForm

class scanner(ScannerForm):
    def __init__(self, scan_param):
        super().__init__(scan_param)

    def scan(self):
        """
        parameters = {
            "ports": "<String in nmap formatting stating strings>"
        }
        """
        
        nmap = nmap3.Nmap()
        
        targets = self.scan_param["ip-address"]
        ports = self.scan_param["packets"]["parameters"]["ports"]
        for ip in targets:
            version_results = nmap.nmap_version_detection(ip, args="-Pn -p "+ports)
            
            print(version_results)
        

    def get_name():
        return "TCP banner grab"

