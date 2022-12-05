#base file
from importlib import import_module



def scanner(scan):
    """
    {
        "targets" : {
            "ips" :[<individual ips entered in>]
            "ip-range": [
                {
                    "start": <start of ip range>
                    "end": <end of ip range>
                },
                {
                    "start": <start of ip range>
                    "end": <end of ip range>
                }

            ]
        },
        "scan-rate" : {
            "max-rate": <int>,
            "min-rate": <int>,
            "scan-delay": <int>
        },
        "repeats" : {
            "count" : <int>,
            "interval": <int>,
            "mode": batch/individual
        },
        "scanner": {
            "type" : <string>,
            "parameters": <object>
        }
    }    
    
    scan = {
        "targets": {
            "ips": [ "192.168.1.234", "192.168.1.238", "192.168.1.134"]
        },
        "type": "snmp",
        "parameters": {
            "SNMP_request" : "get",
            "OID" : "1.3.6.1.2.1.1.2.0",
            "src_port" : "161"
        }
    }
    """
    scan_type = scan["type"]
    mod = scan_mod[scan_type]
    scanner = eval("mod."+scan_type+"(scan)")
    scanner.scan()
    """
    for ip in scan["targets"]["ips"]:
        parameters = scan["parameters"]
        scanner = eval("mod."+scan_type+"(ip, parameters)")
        scanner.scan()
    """

def module_discover():
    f = open("configuration.yaml","r")
    """
    {
        <scan_type> : (imported module)
    }    
    """
    global scan_mod ={}
    for mod in f:
        scan_type = mod.split()[0]
        scan_mod[scan_type] = import_module(scan_type)
    return scan_mod



if __name__ == "__main__":
    scanner()