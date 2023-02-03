#base file
from importlib.machinery import SourceFileLoader
import os


def scanner(scan_param):
    """
    "ip-ranges": {
			"type": "array",
            "items": {
			  "type": "object",
			  "properties" : {
                "start": {
		          "type": "string",
			      "format": "string"
		        },
		        "end": {
			      "type": "string",
			      "format": "string"
		        }
			  }
			}
		  },
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
        "repeats" : {
            "count" : <int>,
            "delay": <int>
        },
        "packets": {
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
    scan_type = scan_param["packets"]["type"]
    mod = scan_mod[scan_type]
    scanner = mod.scanner(scan_param)
    scanner.scan()

def module_discover():
    
    """
    {
        <scan_type> : (imported module)
    }    
    """
    global scan_mod
    
    module_dir = os.listdir()
    os.chdir('Modules')
    dir_list = os.listdir()
    modules = module_list(dir_list)
    
    scan_mod = {}
    for mod in modules:
        print(mod["name"])
        loaded_module = SourceFileLoader(mod["name"], mod["path"]).load_module()
        
        scan_name = loaded_module.scanner.get_name()
        scan_mod[scan_name] = loaded_module
    return scan_mod

def module_list(dir_list):
    filter_list = []
    for file in dir_list:
        if file.endswith(".py"):
            file_entry = {}
            file_entry["path"] =  file
            file_entry["name"] = file[:-3]
            filter_list.append(file_entry)
    return filter_list

if __name__ == "__main__":
    module_discover()
    """
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
    """
    scan = {
        "type": "mdns",
        "parameters": {
            "service": "_ipps._tcp.local."
        }
    }
    """
    """
    scan = {
        "targets": {
            "ips": [ "192.168.1.234", "192.168.1.238", "192.168.1.134"]
        },
        "type": "nmap",
        "parameters": {
            "ports" : "70,80,100"
        }
    }
    """

    scan = {
        "targets": {
            "ips": [ "192.168.1.234"]
        },
        "type": "snmpv10",
        "parameters": {
            "SNMP_request" : "get",
            "OID" : "1.3.6.1.2.1.1.5.0",
            "src_port" : "161"
        }
    }
    scanner(scan)
 