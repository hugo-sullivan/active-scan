from zeroconf import ServiceBrowser, ServiceListener, Zeroconf, ZeroconfServiceTypes
from time import sleep
from scanInterface import ScannerForm

class scanner(ScannerForm):
    def __init__(self, scan_param):
        super().__init__(scan_param)

    def scan(self):
        """
        parameters = {
            "service": "<service being investigate>"
        }
        """
        
        zeroconf = Zeroconf()
        listener = MyListener()
        #browser = asyncio.AsyncServiceBrowser(zeroconf, ["_http._tcp.local."], listener, )
        
        service = self.scan_param["parameters"]["service"]
        browser = ServiceBrowser(zeroconf, service, listener, question_type=2)
        try:
            input("Press enter to exit...\n\n")
        finally:
            zeroconf.close()



class MyListener(ServiceListener):

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        pass

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        pass

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        print(f"Service {name} added, service info: {info}")


"""
"__googlecast._tcp.local."
"_services._dns.-sd.udp.local."
"_pdl-datastream._tcp.local."
"_ipp._tcp.local."
"_http._tcp.local."
"_scanner._tcp.local."
"_http-alt._tcp.local."
"_uscan._tcp.local."
"_ipps._tcp.local."
"_privet._tcp.local."
"_uscans._tcp.local."
"""