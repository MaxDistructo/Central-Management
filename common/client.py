from utils.logger import Logger

logger = Logger("Client")
threads = list()

class CommonClient:
    db_connection = ""
    def __init__(self):
        print("Starting Up")

    def main(self):
        print("Common Main")