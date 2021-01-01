from common.client import CommonClient as common_client
from utils.logger import Logger
import common.config as cfg

logger = Logger("Client")
threads = list()

class Client(common_client):
    device_def = None

    def __init__(self):
        super().__init__()
        self.db_connection = db.connect(cfg.server_ip, cfg.username, cfg.password, cfg.port)
    
    def main(self):
        super().main()
        logger.info("Client Main")

    def install_program(self):

