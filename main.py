from common.operating_systems import *
import db
from utils.logger import Logger
from server import start as server_start
from client.client import Client as client_start

side = ""

def main():
    logger = Logger("CentralManagement")
    logger.info("Starting CentralManagement")
    logger.info("Attempting to Setup DB")
    db.setup_db()
    if side == "server":
        server_start
    elif side == "client":
        client_start

if __name__ == "__main__":
    main()