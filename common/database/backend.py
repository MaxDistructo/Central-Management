from common.device_defs.system import System
from common.device_defs.device import Device
from utils.logger import Logger

class Backend:
    logger: Logger = Logger("")
    file_path = ""
    def __init__(self):
        print()
    def add_computer(self, system: System) -> bool:
        print("ERROR - Please implement the function: Backend.add_computer(self, system: System)")
    def remove_computer(self, system: System) -> bool:
        print("ERROR - Please implement the function: Backend.remove_computer(self, system: System)")
    def add_device(self, device: Device) -> bool:
        print("ERROR - Please implement the function: Backend.add_device(self, device: Device)")
    def remove_device(self, device: Device) -> bool:
        print("ERROR - Please implement the function: Backend.remove_device(self, device: Device)")
    def query_computer(self, query: str) -> list:
        print()
    def save_state(self, file=file_path):
        print()
    def read_state(self, file=file_path):
        print()
    def set_file_path(self, path):
        print()
    def get_file_path(self):
        return self.file_path