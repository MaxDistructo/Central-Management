from common.operating_systems import *
from common.database.db import Database
from common.database.db import get_database
from utils.logger import Logger
from server.start import ServerClient as server_start
from client.client import Client as client_start
from common.client import CommonClient
import logging.log as log
import server.server
import client.client
import atexit

side = ""
db: Database = None
client: CommonClient = None

atexit.register(exit)

def main():
    logger = Logger("CentralManagement")
    logger.info("Starting CentralManagement")
    if side == "server":
        db = get_database("json")
        client = server_start()
    elif side == "client":
        client = client_start()
    elif side == "administrative_client":
        print("not implemented")

if __name__ == "__main__":
    main()

def exit():
    for thread in client.threads:
        thread.join()
        if client is server_start:
            client.exit()
    for thread in log.threads:
        thread.join()