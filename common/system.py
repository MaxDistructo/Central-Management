import common.operating_systems.os_info
import ipaddress
import socket

class System:
    os_info = ""
    hostname = ""
    ip_address = ""
    
    def __init__(self, os_info, hostname=get_hostname(os_info), ip_address=get_ip()):
        self.os_info = os_info
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

    def __str__(self):
        return f"common.system.System({self.os_info.__str__()}, {self.hostname}, {self.ip_address})"


    
    