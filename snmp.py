from pysnmp import hlapi

"""
def main():
    #args = sys.argv[1:]
    #IP = input("Enter the desired IP address: ")
    IP = "192.168.1.234"
    OID = []    
    OID_input = input("Enter the desired OID: ")
    outputs = ["SNMP outputs"]
    
    if (IP.split()[0] == "-f"):
        #python open file then loop through the for loops
        f = open(IP.split()[1], "r")
        IP_file  = f.read().split()
        for target in IP_file:
            outputs.append(get(target, OID, hlapi.CommunityData('public')))
            print(target)
	
    else:

    if (OID_input.split()[0] == "-b"):
        bulk_non_repeaters = int(input("Enter the desired no repeater value: "))
        bulk_max_repeaters = int(input("Enter the desired max repeater value: "))
        OID.append(OID_input.split()[1])
        outputs.append(get_bulk(IP,OID,hlapi.CommunityData('public'),bulk_max_repeaters,bulk_non_repeaters))
    else:
        OID.append(OID_input)
        outputs.append(get(IP, OID, hlapi.CommunityData('public')))
	
    for response in outputs:
        print(response)
        print("\n")
"""

def snmp_get(desc):
    """
    desc = {
        type = "SNMP",
        SNMP_request = "get"/"get_bulk",
        OID = ""(OID trying to investigate),
        bulk_non_repeaters = int(),
        bulk_max_repeaters = int(),
        IPs = [],
        src_port = ""
    }
    """
    if (desc["SNMP_request"] == "get"):
        for ip in desc["IPs"]:
            get(ip, desc["OID"], hlapi.CommunityData('public'), desc["src_port"])
    elif(desc["SNMP_request"] == "get_bulk"):
        for ip in desc["IPs"]:
            get_bulk(ip, desc["OID"], hlapi.CommunityData('public'), desc["bulk_max_repeaters"], desc["bulk_non_repeaters"], desc["src_port"])



def get_bulk(target, oids, credentials, count, start_from=0, port=161,
             engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.bulkCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        start_from, count,
        *construct_object_types(oids)
    )
    return fetch(handler, count)

def get(target, oids, credentials, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.getCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        #hlapi.ObjectType(hlapi.ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
        *construct_object_types(oids)
    )
    return fetch(handler, 1)[0]
    
def construct_object_types(list_of_oids):
    object_types = []
    for oid in list_of_oids:
        object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))
    return object_types

def cast(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            try:
                return str(value)
            except (ValueError, TypeError):
                pass
    return value

def fetch(handler, count):
    result = []
    for i in range(count):
        try:
            error_indication, error_status, error_index, var_binds = next(handler)
            if not error_indication and not error_status:
                items = {}
                for var_bind in var_binds:
                    items[str(var_bind[0])] = cast(var_bind[1])
                result.append(items)
            else:
                raise RuntimeError('Got SNMP error: {0}'.format(error_indication))
        except StopIteration:
            break
    return result
