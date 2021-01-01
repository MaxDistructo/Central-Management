from common.device_defs.device import Device
from common.device_defs.system import System
from utils.logger import Logger
import socket
logger = Logger("Client")


class DB_Connection():
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = ""
    port = ""
    username = ""
    password = ""

    def __init__(self, ip, port, username, password):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        self.socket.bind((self.ip, self.port))
        print("unimplemented")

    def add_computer(self, system: System) -> bool:


    def remove_computer(self, system: System) -> bool:


    def add_device(self, device: Device) -> bool:


    def remove_device(self, device: Device) -> bool:


    def query_computer(self, query: str) -> list:


    def save_state(self, file=super.get_file_path()):


    def read_state(self, file=super.get_file_path()):



class CommonClient:
    db_connection: DB_Connection = None
    threads = list()

    def __init__(self):
        print("Starting Up")

    def main(self):
        print("Common Main")

    def exit(self):
        print("")



