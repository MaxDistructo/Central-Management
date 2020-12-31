# Python Libs
import socket
import threading
import concurrent.futures

# Our Code
from utils.logger import Logger
import common.config as cfg
import common.database.db as database
from common.database.db import Database
from utils.checks import is_valid_macaddr802 as ValidateMAC
from utils.checks import string_check as ValidateString

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
        logger.info(f"Creating DB_Server on localhost:{cfg.port}")
        self.database_instance = database.get_database("json")
        self.state = 1 #Setting Up
        self.sock.bind(self.server_address)
        self.sock.listen(1)

    def start(self):
        logger.info("Starting DB_Server")
        self.state = 2 #Starting Server
        
        #Starting the server will create multiple processing threads on the one socket
        #Initially will only use 4 threads although this may expand
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(self.process_request, range(4))
        
        #We only want 1 db update thread to thread-safe our updates to the DB. This needs to be kept track of separately.
        db_update_thread = threading.Thread(target=self.update_db, args=(1,))
        self.threads.append(db_update_thread)
        db_update_thread.start()
        
        logger.debug("Sucessfully started DB_Server")
        self.state = 3 #Running
    
    def process_request(self,name):
        logger.debug(f"Starting Server Thread {name}")
        while self.state >= 2: #We allow ourself to accept requests as long as we are in a runnable state 
            connection, client_address = self.sock.accept()
    
    def update_db(self,name): #Thread safe our DB writes
        # Operation Syntax: [r,w,a],[identifier],[value_to_update],[value]
        split = self.queue.remove(self.queue[0])
        error_state = False
            
        #TODO: Safety Check the Split so we don't write garbage data to the db
        if not ValidateMAC(split[1]): # 1 should be a MAC address identifier
            error_state = True
            logger.error(f"Invalid input recieved! - {split}")
        if not ValidateString(split[2]): # 2 should be a string of some kind
            error_state = True
            logger.error(f"Invalid input recieved! - {split}")
        if not ValidateString(split[3]): # 3 should be a string of some kind
            error_state = True
            logger.error(f"Invalid input recieved! - {split}")
        
        # If this input passes the validation checks, write/append to the database. Otherwise we ignore the input
        if not error_state:
            if split[0] == "w":
                self.db[split[1]][split[2]] = split[3]
            elif split[0] == "a":
                self.db[split[1]][split[2]] += split[3]
        
        #Operation has been performed/ignored and is dropped from the queue
        self.queue.remove(self.queue[0])
    
    def read_db(self, id, value) -> str:
        print("unimplemented")
        return ""
