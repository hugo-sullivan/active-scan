#base file
from scanTranslator import ScannerForm
from importlib import import_module



def main():
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
    """
    scan = {
        "targets": {
            "ips": [ "192.168.1.234", "192.168.1.238", "192.168.1.134"]
        },
        "type": "snmp",
        "parameters": {
            "SNMP_request" : "get",
            "OID" : "1.3.6.1.2.1.1.1.0",
            "src_port" : "161"
        }
    }
    
    mod = import_module(scan["type"])
    for ip in scan["targets"]["ips"]:
        parameters = scan["parameters"]
        scan_type = scan["type"]
        scanner = eval("mod."+scan_type+"(ip, parameters)")
        scanner.get()

if __name__ == "__main__":
    main()