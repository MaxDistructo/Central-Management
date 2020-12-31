import threading
from datetime import datetime
from utils.logger import Logger

log_queue = list()
threads = list()
logger = Logger("Log")

def __init__():
    db_update_thread = threading.Thread(target=logging_thread, args=(1,))
    threads.append(db_update_thread)
    db_update_thread.start()

def logging_thread(name):
    logger.info(f"Starting Log Writer Thread #{name}")
    log, log_entry = log_queue[0].split(" ")
    update_log(log, log_entry)

def update_log(log, log_entry):
    file = open(log, "a")
    time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    file.write(f"[{time}] {log_entry}")
    file.close()

def log(log, log_entry):
    log_queue.append(f"{log},{log_entry}")