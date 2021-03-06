from common.client import CommonClient as common_client
from common.client import DB_Connection
from utils.logger import Logger
from server.server import DB_Server
import common.config as cfg

logger = Logger("Server")
db = None


class ServerClient(common_client):
    db_server = None

    def __init__(self):
        super().__init__()
        
        #Create DB Connection
        self.db_connection = DB_Connection("localhost", cfg.port, cfg.username, cfg.password)
        #Create DB Server
        self.db_server = DB_Server()
        
        #self.db_connection = db.connect("localhost", cfg.username, cfg.password, cfg.port)

    def main(self):
        super().main()
        print("Server Main")

        #Start the DB_Server
        self.db_server.start()
        
        #Connect to our own DB Server to finish the chain of command
        self.db_connection.connect()
    
    def exit(self):
        # Pass through that we are exiting to the db_server so that the accept threads stop taking requests.
        self.db_server.state = 1
