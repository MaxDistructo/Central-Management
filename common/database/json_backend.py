import json

from utils.logger import Logger
from common.database.backend import Backend
from common.device_defs.system import System
from common.device_defs.device import Device
from common.operating_systems.os_info import OS_Info
from common.device_defs.system import construct_from_json as system_json_construct
from common.device_defs.device import construct_from_json as device_json_construct

class JSONBackend(Backend):
    json = {}
    def __init__(self, input_file=read_state()):
        self.logger = Logger("JSONBackend")
        self.logger.info("Initializing JSONBackend")
        self.json = input_file
        self.file_path = "db/database.json"

    def query_computer(self, query: str) -> list:
        matching = []
        for pc in self.json:
            if pc["type"] == "system":
                sys = system_json_construct(self.json[pc])
                if sys.mac_address.__contains__(query):
                    matching + sys
                if sys.custom_name.__contains__(query):
                    matching + sys
                if sys.hostname.__contains__(query):
                    matching + sys
                if sys.ip_address.__contains__(query):
                    matching + sys
            elif pc["type"] == "device":
                dev = device_json_construct(self.json[pc])
                if dev.mac_address.__contains__(query):
                    matching + dev
                if dev.custom_name.__contains__(query):
                    matching + dev
                if dev.hostname.__contains__(query):
                    matching + dev
                if dev.ip_address.__contains__(query):
                    matching + dev
        return matching

    def add_computer(self, system: System) -> bool:
        self.json[system.mac_address] = {system.__to_json__()}
    
    def remove_computer(self, system: System) -> bool:
        system.disable()
        self.json[system.mac_address] = {system.__to_json__()}
    
    def add_device(self, device: Device) -> bool:
        self.json[device.mac_address] = {device.__to_json__()}
    
    def remove_device(self, device: Device) -> bool:
        device.disable()
        self.json[device.mac_address] = {device.__to_json__()}
    
    def save_state(self, file=super.get_file_path()):
        db = open(file,'w')
        db.write(json.dumps(self.json))
        db.close()

    def read_state(self, file=super.get_file_path()):
        try:
            db = open(file,"r")
            self.logger.info("Successfully loaded Database")
            self.json = json.loads(db.readlines())
            db.close()
        except:
            self.logger.error("Unable to open Database!")
            self.logger.info("Initializing Empty Database")
            self.json = {}

    def set_file_path(self, path):
        self.file_path = path