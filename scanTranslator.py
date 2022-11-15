from snmp import *

def getScanner(scanType, target, parameters):
    if (scanType == "snmp"):
        return Snmp(target,parameters)
    else:
        print("Invalid scan type")
        return 
	