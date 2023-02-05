import time
import threading
from scan_db import get_next_scan, get_scan, update_scan
from actscan import scanner, module_discover


class scan_control_thread(threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)

   def run(self):
    module_discover()
    while True:
        scan_id, scan_time = get_next_scan()
        if (scan_id != None and scan_time <= time.time()):
            scan_handler(scan_id)
        else:
            #print("no scans to complete")
            time.sleep(1)
    
    
def scan_handler(scan_id):
    print("scan to complete "+str(scan_id))
    update_scan(scan_id)
    scan = get_scan(scan_id)
    print(scan)
    scanner(scan)
    update_scan(scan_id)
    
    print("completed "+str(scan_id))
