from time import sleep
import urllib.request

from ssdpy import SSDPClient

from scanInterface import ScannerForm

class ssdp(ScannerForm):

    def __init__(self, target, parameters):
        super().__init__(target,parameters)
    
    def scan()
        client = SSDPClient()
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
