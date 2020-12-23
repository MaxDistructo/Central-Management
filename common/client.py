import common.db
from utils.logger import Logger

logger = Logger("Client")

class CommonClient:
    db_connection = ""
    def __init__(self):
        print("Starting Up")

    def main(self):
        print("Common Main")