from time import sleep
import urllib.request
import ssdpy

from scanInterface import ScannerForm

class scanner(ScannerForm):
    
    def scan(self):
        """
        parameters = {
            "mx": <int 1-5>
        }
        """
        
        if ("mx" in self.scan_param["packets"]["parameters"]):
            mx = self.scan_param["packets"]["parameters"]["mx"]
        else:
            mx = 1
        
        client = ssdpy.SSDPClient()
        devices = client.m_search("ssdp:all", mx)
        for device in devices:
            print(device)
            if ("location" in device):
                getXML(device["location"])

    def get_name():
        return "ssdp"

def getXML(location):
    print(location)
    if (location != None):
        contents = urllib.request.urlopen(location).read()
        print("Content",contents)
    

