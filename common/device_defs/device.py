from utils.logger import Logger

class Device:
    ip_address = ""
    hostname = ""
    custom_name = ""
    mac_address = ""
    logger = ""
    enabled = True
    
    def __init__(self, ip_address, hostname, custom_name, mac_address, enabled=True):
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

    def __to_json__(self) -> dict:
        return {"type":"device","ip_address":self.ip_address, "hostname":self.hostname, "custom_name":self.custom_name, "mac_address":self.mac_address, "enabled":self.enabled}

    def disable(self):
        if(self.enabled):
            self.enabled = False
    
    def enable(self):
        if(not self.enabled):
            self.enabled = True

def construct_from_json(backend_json: dict):
    return Device(backend_json["ip_address"], backend_json["hostname"], backend_json["custom_name"], backend_json["mac_address"], backend_json["enabled"])