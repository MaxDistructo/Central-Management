from common.client import CommonClient as common_client
from utils.logger import Logger
import common.db as db
import common.config as cfg

logger = Logger("Server")

class ServerClient(common_client):
    def __init__(self):
        super().__init__()
        db.init_server()
        self.db_connection = db.connect("localhost", cfg.username, cfg.password, cfg.port)

    def main(self):
        super().main()
        print("Server Main")
        db.start_db()