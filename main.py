from common.operating_systems import *
from common.database.db import Database
from common.database.db import get_database
from utils.logger import Logger
from server.start import ServerClient as server_start
from client.client import Client as client_start
from common.client import CommonClient

side = ""
db: Database = None
client: CommonClient = None

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
    db.exit()