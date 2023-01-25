import json
import time
import threading


"""
    {
    "sheduled" :{
        <scan_id in> : {
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
                },
                "scheduled_time": <time scheduled for>
            }
        },
    "running : {<scan_id in> : {
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
                },
                "scheduled_time": <time scheduled for>
                "start_time": <time when scan was moved into running>
            }
        },
    "past" : {
        <scan_id in> : {
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
                },
                "scheduled_time": <run time initially given>
                "start_time": <time first updated>,
                "finish_time": <time seconded updated running>
            }
        }
    }
    "scan_number": <int>
    """
def load_db(scan_file):
    with open(scan_file, "r") as read_file:
        data = json.load(read_file)
    global database
    database = data
    
def save_db(scan_file):
    with open(scan_file, "w") as write_file:
        json.dump(database, write_file)

def add_scan(new_scan):
    scan_id = database["scan_number"]
    database["scheduled"][scan_id] = new_scan
    database["scan_number"] = scan_id+1
    
def edit_scan(scan_id, updated_scan):
    if (scan_id in database["scheduled"]):
        database["scheduled"][scan_id] = updated_scan

def delete_scan(scan_id):
    database["scheduled"].pop(scan_id)

def update_scan(scan_id):
    if (scan_id in database["scheduled"]):
        scan = database["scheduled"].pop(scan_id)
        scan["start_time"] = time.time()
        database["running"][scan_id] = scan  
        
    elif(scan_id in database["running"]):
        scan = database["running"].pop(scan_id)
        scan["finish_time"] = time.time()
        database["past"][scan_id] = scan

def get_scheduled_scans():
    return database["scheduled"]

def get_scan(scan_id):
    scan = None
    if (scan_id in database["scheduled"]):
        scan = database["scheduled"][scan_id]
    elif (scan_id in database["running"]):
        scan = database["running"][scan_id]
    elif (scan_id in database["past"]):
        scan = database["past"][scan_id]
    return scan

def get_next_scan():
    next_scan_time = None
    next_scan_id = None
    for scan_id in database["scheduled"]:
        scan_time = database["scheduled"][scan_id]["scheduled_time"]
        if (next_scan_id == None or scan_time < next_scan_time):
            next_scan_id = scan_id
            next_scan_time = scan_time
    return next_scan_id, next_scan_time

def get_running_scans():
    return database["running"]

def get_previous_scans():
    print("Gets the previous scan")
    return database["past"]
    
def database_init():
    global database
    database = {}
    database["scheduled"] = {}
    database["running"] = {}
    database["past"] = {}
    database["scan_number"] = 0
    

if __name__ == "__main__":
    """
    database_init()
    scan_0 = {
        "targets": {
            "ips": ["192.168.1.2","192.168.1.119","192.168.1.156","192.168.1.179","192.168.1.196","192.168.1.197","192.168.1.198","192.168.1.214","192.168.1.219", "192.168.1.234","192.168.1.238", "192.168.1.241","192.168.1.247"]
        },
        "type": "snmp",
        "parameters": {
            "SNMP_request" : "get",
            "OID" : "1.3.6.1.2.1.1.2.0",
            "src_port" : "161"
        },
        "scheduled_time": (time.time())
    }
    scan_1 = {
        "targets": {
            "ips": ["192.168.1.2","192.168.1.119","192.168.1.156","192.168.1.179","192.168.1.196","192.168.1.197","192.168.1.198","192.168.1.214","192.168.1.219", "192.168.1.234","192.168.1.238", "192.168.1.241","192.168.1.247"]
        },
        "parameters": {
            "ports" : "20,21,22,80,135,139,445"
        },
        "type": "nmap",
        "scheduled_time": (time.time())
    }
    scan_2 = {
        "targets": {
            "ips": ["192.168.1.234","192.168.1.238"]
        },
        "type": "snmp",
        "parameters": {
            "SNMP_request" : "get",
            "OID" : "1.3.6.1.2.1.1.1.0",
            "src_port" : "161"
        },
        "scheduled_time": (time.time())
    }
    scan_3 = {
        "targets": {
            "ips": ["192.168.1.234","192.168.1.238"]
        },
        "type": "snmp",
        "parameters": {
            "SNMP_request" : "get",
            "OID" : "1.3.6.1.2.1.1.3.0",
            "src_port" : "161"
        },
        "scheduled_time": (time.time())
    }
    scan_4 = {
        "targets": {
            "ips": ["192.168.1.234","192.168.1.238"]
        },
        "type": "snmp",
        "parameters": {
            "SNMP_request" : "get",
            "OID" : "1.3.6.1.2.1.1.4.0",
            "src_port" : "161"
        },
        "scheduled_time": (time.time())
    }
    scan_5 = {
        "targets": {
            "ips": ["192.168.1.234","192.168.1.238"]
        },
        "type": "snmp",
        "parameters": {
            "SNMP_request" : "get",
            "OID" : "1.3.6.1.2.1.1.5.0",
            "src_port" : "161"
        },
        "scheduled_time": (time.time())
    }
    scan_5 = {
        "targets": {
            "ips": ["192.168.1.234","192.168.1.238"]
        },
        "type": "snmp",
        "parameters": {
            "SNMP_request" : "get",
            "OID" : "1.3.6.1.2.1.1.6.0",
            "src_port" : "161"
        },
        "scheduled_time": (time.time())
    }
    scan_18 = {
        "targets": {
            "ips": ["192.168.1.234","192.168.1.238"]
        },
        "type": "snmp",
        "parameters": {
            "SNMP_request" : "get",
            "OID" : "1.3.6.1.2.1.25.3.2.1.3.1",
            "src_port" : "161"
        },
        "scheduled_time": (time.time())
    }
    scan_6 = {
        "targets": {
            "ips": ["192.168.1.234","192.168.1.238"]
        },
        "type": "snmp",
        "parameters": {
            "SNMP_request" : "get_bulk",
            "OID" : "1.3.6.1.2.1.17.1.4.1.2",
            "src_port" : "161",
            "bulk_max_repeaters" : 21,
            "bulk_non_repeaters" : 0
        },
        "scheduled_time": (time.time())
    }
    scan_7 = {
        "type": "mdns",
        "parameters": {
            "service": "_ipps._tcp.local."
        },
        "scheduled_time": (time.time())
    }
    scan_8 = {
        "type": "mdns",
        "parameters": {
            "service": "__googlecast._tcp.local."
        },
        "scheduled_time": (time.time())
    }
    scan_9 = {
        "type": "mdns",
        "parameters": {
            "service": "_services._dns.-sd.udp.local."
        },
        "scheduled_time": (time.time())
    }
    scan_10 = {
        "type": "mdns",
        "parameters": {
            "service": "_pdl-datastream._tcp.local."
        },
        "scheduled_time": (time.time())
    }
    scan_11 = {
        "type": "mdns",
        "parameters": {
            "service": "_http._tcp.local."
        },
        "scheduled_time": (time.time()+20)
    }
    scan_12 = {
        "type": "mdns",
        "parameters": {
            "service": "_scanner._tcp.local."
        },
        "scheduled_time": (time.time()+20)
    }
    scan_13 = {
        "type": "mdns",
        "parameters": {
            "service": "_http-alt._tcp.local."
        },
        "scheduled_time": (time.time()+20)
    }
    scan_14 = {
        "type": "mdns",
        "parameters": {
            "service": "_uscan._tcp.local."
        },
        "scheduled_time": (time.time()+20)
    }
    scan_15 = {
        "type": "mdns",
        "parameters": {
            "service": "_privet._tcp.local."
        },
        "scheduled_time": (time.time()+20)
    }
    scan_16 = {
        "type": "mdns",
        "parameters": {
            "service": "_uscans._tcp.local."
        },
        "scheduled_time": (time.time()+20)
    }
    scan_17 = {
        "type": "ssdp",
        "scheduled_time": (time.time())
    }
    
    add_scan(scan_0)
    add_scan(scan_1)
    add_scan(scan_2)
    add_scan(scan_3)
    add_scan(scan_4)
    add_scan(scan_5)
    add_scan(scan_6)
    add_scan(scan_7)
    add_scan(scan_8)
    add_scan(scan_9)
    add_scan(scan_10)
    add_scan(scan_11)
    add_scan(scan_12)
    add_scan(scan_13)
    add_scan(scan_14)
    add_scan(scan_15)
    add_scan(scan_16)
    add_scan(scan_17)
    """
    load_db("database.json")
    scan_thread = scan_control_thread()
    scan_thread.start()
    
