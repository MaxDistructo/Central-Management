from common.operating_systems.os_info import OS_Info as OI
import socket

class System:
    os_info: OI = OI("","","")
    hostname = ""
    custom_name = ""
    ip_address = ""
    mac_address = ""
    
    def __init__(self, oi: OI, hostname=get_hostname(os_info), ip_address=get_ip()):
        self.os_info = oi
        self.hostname = hostname
        self.ip_address = ip_address
    
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
        return {"os_info":self.os_info.__to_json__(), }

    def __str__(self):
        return f"common.system.System({self.os_info.__str__()}, {self.hostname}, {self.ip_address})"


    
    