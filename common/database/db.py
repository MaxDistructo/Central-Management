from utils.logger import Logger
from common.database.backend import Backend
from common.database.json_backend import JSONBackend
from common.database.mysql_backend import MysqlBackend
from common.device_defs.device import Device
from common.device_defs.system import System

logger = Logger("Database")

class Database:
    backend = Backend()
    def __init__(self, backend: Backend):
        logger.info("Initializing the Database")
        self.backend = backend
    
    # Below is wrapper functions that directly correlate to the backend methods.
    def add_computer(self, system: System) -> bool:
        return self.backend.add_computer(system)

    def remove_computer(self, system: System) -> bool:
        return self.backend.remove_computer(system)

    def add_device(self, device: Device) -> bool:
        return self.backend.add_device(device)

    def remove_device(self, device: Device) -> bool:
        return self.backend.remove_device(device)
    
    def query_computer(self, query: str) -> list:
        return self.backend.query_computer(query)
    
    def save_state(self, file=super.get_file_path()):
        return self.backend.save_state(file)
    
    def read_state(self, file=super.get_file_path()):
        return self.backend.read_state(file)
    
    def set_file_path(self, path):
        self.file_path = path
    
    def exit(self):
        self.backend.save_state()

def get_database(type: str) -> Database:
    if type == "json":
        return Database(JSONBackend())
    elif type == "sql":
        return Database(MysqlBackend())
    else:
        logger.critical("Invalid Database Type specified!")
        exit()
    
