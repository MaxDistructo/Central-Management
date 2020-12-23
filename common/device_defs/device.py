from utils.logger import Logger

class Device:
    ip_address = ""
    hostname = ""
    custom_name = ""
    mac_address = ""
    logger = ""
    
    def __init__(self, ip_address, hostname, custom_name, mac_address):
        self.ip_address = ip_address
        self.hostname = hostname
        self.custom_name = custom_name
        self.mac_address = mac_address
        self.logger = Logger(f"[{self.get_display_name()}]")
    
    def get_display_name(self) -> str:
        if self.custom_name == "":
            return self.hostname
        else:
            return self.custom_name
    
    def __str__(self) -> str:
        return f"Device({self.ip_address},{self.hostname},{self.custom_name},{self.mac_address})"