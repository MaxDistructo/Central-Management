from utils.logger import Logger
from common.client import CommonClient, DB_Connection
import logging.log as log
import atexit
import common.config as cfg

# Deal with Siding imports
side = cfg.side
if side == "server":
    from server.start import ServerClient as Client
elif side == "client":
    from client.client import Client

db: DB_Connection = None
client: CommonClient = None
atexit.register(exit)


def main():
    global client
    global db
    logger = Logger("CentralManagement")
    logger.info("Starting CentralManagement")
    client = Client()
    client.db_connection.connect()
    db = client.db_connection
    client.main()


if __name__ == "__main__":
    main()


def exit():
    for thread in client.threads:
        thread.join()
        client.exit()
    for thread in log.threads:
        thread.join()
