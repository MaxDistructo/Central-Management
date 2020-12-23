import json

from utils.logger import Logger
from common.database.backend import Backend
from common.device_defs.system import System
from common.device_defs.device import Device

class JSONBackend(Backend):
    json = {}
    file_path = "db/database.json"
    def __init__(self, input_file={}):
        self.logger = Logger("JSONBackend")
        self.logger.info("Initializing JSONBackend")
        self.json = input_file

    def add_computer(self, system: System) -> bool:
        self.json[system.mac_address] = {"os_info":f"{system.os_info.__str__()}",""}
    
    def remove_computer(self, system: System) -> bool:
        print("ERROR - Please implement the function: Backend.remove_computer(self, system: System)")
    
    def add_device(self, device: Device) -> bool:
        print("ERROR - Please implement the function: Backend.add_device(self, device: Device)")
    
    def remove_device(self, device: Device) -> bool:
        print("ERROR - Please implement the function: Backend.remove_device(self, device: Device)")
    
    def save_state(self, file=file_path):
        db = open(file,'w')
        db.write(json.dumps(self.json))
        db.close()

    def read_state(self, file=file_path):
        db = open(file,"r")
        self.json = json.loads(db.readlines())
        db.close()

    def set_file_path(self, path):
        self.file_path = path