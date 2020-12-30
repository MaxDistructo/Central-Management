import socket
from utils.logger import Logger
import common.config as cfg
import threading
import concurrent.futures
import common.database.db as database
from common.database.db import Database

logger = Logger("Server")

class DB_Connection():
    def __init__(self, ip, port, username, password):
        print("unimplemented")
    def connect(self):
        print("unimplemented")

class DB_Server():
    logger = Logger("Database Server")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", cfg.port) #Listen on all interfaces
    state = 0 #OFF
    threads = list()
    queue = list()
    db = dict()
    database_instance: Database = None

    def __init__(self):
        logger.info(f"Starting up on localhost:{cfg.port}")
        self.database_instance = database.get_database("json")
        self.state = 1 #Setting Up
        self.sock.bind(self.server_address)
        self.sock.listen(1)

    def start(self):
        self.state = 2 #Starting Server
        #Starting the server will create multiple processing threads on the one socket
        #Initially will only use 4 threads although this may expand
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(self.process_request, range(4))
        db_update_thread = threading.Thread(target=self.update_db, args=(1))
        self.state = 3 #Running
    
    def process_request(self,name):
        logger.info(f"Starting Server Thread {name}")
        while self.state >= 2: #We allow ourself to accept requests as long as we are in a runnable state 
            connection, client_address = self.sock.accept()
    
    def update_db(self): #Thread safe our DB writes
        for operation in self.queue:
            # Operation Syntax: [r,w,a],[identifier],[value_to_update],[value]
            split = operation.split(",")
            if split[0] == "w":
                self.db[split[1]][split[2]] = split[3]
            elif split[0] == "a":
                self.db[split[1]][split[2]] += split[3]
    def read_db(self, id, value) -> str:
        print("unimplemented")
        return ""
