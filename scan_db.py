import json
import time


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
    return database["past"]
    
def database_init():
    global database
    database = {}
    database["scheduled"] = {}
    database["running"] = {}
    database["past"] = {}
    database["scan_number"] = 0
    

if __name__ == "__main__":
    database_init()
    scan_0 = {
        "targets": {
            "ips": [ "192.168.1.234", "192.168.1.238", "192.168.1.134"]
        },
        "type": "snmp",
        "parameters": {
            "SNMP_request" : "get",
            "OID" : "1.3.6.1.2.1.1.2.0",
            "src_port" : "161"
        },
        "scheduled_time": (time.time()+10)
    }
    scan_1 = {
        "targets": {
            "ips": [ "192.168.1.7"]
        },
        "type": "snmp",
        "parameters": {
            "SNMP_request" : "get",
            "OID" : "1.3.6.1.2.1.1.2.0",
            "src_port" : "161"
        },
        "scheduled_time": (time.time()+20)
    }
    add_scan(scan_0)
    add_scan(scan_1)
    scan_control()
