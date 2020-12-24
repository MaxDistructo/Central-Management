from common.operating_systems.os_info import OS_Info as OI
from common.operating_systems.os_info import construct_from_json as oi_construct_from_json
import socket

class System:
    os_info: OI = OI("","","")
    hostname = ""
    custom_name = ""
    ip_address = ""
    mac_address = ""
    last_logged_in = ""
    enabled = True
    
    def __init__(self, oi: OI, hostname=get_hostname(os_info), ip_address=get_ip(), custom_name="", mac_address="00:00:00:00:00:00", enabled=True, last_logged_in=""):
        self.os_info = oi
        self.hostname = hostname
        self.ip_address = ip_address
        self.custom_name = custom_name
        self.mac_address = mac_address
        self.enabled = enabled
        self.last_logged_in = last_logged_in
    
    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        tmp = s.getsockname()[0]
        s.close()
        return tmp

    def get_hostname(self, os_info):
        return os_info.execute_command("hostname")

    def get_display_name(self) -> str:
        if self.custom_name == "":
            return self.hostname
        else:
            return self.custom_name
    
    def __to_json__(self) -> dict:
        return {"type":"system","os_info": self.os_info.__to_json__(), "hostname": self.hostname, "custom_name": self.custom_name, "ip_address": self.ip_address, "mac_address": self.mac_address, "enabled": self.enabled, "user": self.last_logged_in}

    def __str__(self):
        return f"common.system.System({self.__to_json__()})"

    def disable(self):
        if(self.enabled):
            self.enabled = False
    
    def enable(self):
        if(not self.enabled):
            self.enabled = True

def construct_from_json(backend_json: dict) -> System:
    return System(oi_construct_from_json(backend_json["os_info"]), hostname= backend_json["hostname"], ip_address= backend_json["ip_address"], custom_name = backend_json["custom_name"], mac_address= backend_json["mac_address"], enabled= backend_json["enabled"], last_logged_in = backend_json["user"])