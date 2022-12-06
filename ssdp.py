from time import sleep
import urllib.request
import ssdpy

from scanInterface import ScannerForm

class ssdp(ScannerForm):

    def __init__(self, scan_param):
        super().__init__(scan_param)
    
    def scan(self):
        client = ssdpy.SSDPClient()
        devices = client.m_search("ssdp:all")
        for device in devices:
            print(device)
            if ("location" in device):
                getXML(device["location"])

def getXML(location):
    print(location)
    if (location != None):
        contents = urllib.request.urlopen(location).read()
        print("Content",contents)
    

if __name__ == "__main__":
    scan_param = {
        "type": "ssdp"
    }
    
    scanner = ssdp(scan_param)
    scanner.scan()
