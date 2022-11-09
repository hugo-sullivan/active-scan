#base file
import snmp

def main():
    desc = {
    "type" : "SNMP",
    "SNMP_request" : "get",
    "OID" : "1.3.6.1.2.1.1.2.0",
    "IPs" : ["192.168.0.2","192.168.0.4","192.168.0.5","192.168.0.6","192.168.0.7","192.168.0.8","192.168.0.10"],
    "src_port" : "1000"
    }
    snmp.snmp_get(desc)


if __name__ == "__main__":
    main()