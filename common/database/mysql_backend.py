class MysqlBackend(Backend):
    def __init__(self):
        print("DO NOT USE!")

def connect_central_management() -> connection.MySQLConnection:
    return connection.MySQLConnection(user = "root", password = 'Password01!',
     host = '127.0.0.1', database = 'central_management')

def setup_connect() -> connection.MySQLConnection:
    return connection.MySQLConnection(user = "root", password = 'Password01!',
     host = '127.0.0.1')
     #Don't Specify Database so we can make Databases

def setup_db():
    TABLES = {}
    DB_NAME = "central_management"
    TABLES['users'] = (
        "CREATE TABLE `users` ("
        "   `user_no` int(11) NOT NULL AUTO_INCREMENT,"
        "   `username` varchar(32) NOT NULL,"
        "   `password` varchar(128) NOT NULL"
        ")"
    )
    cnx = setup_connect()
    cursor = cnx.cursor()
    try:
        logger.debug("Checking if Database Exists")
        check_for_database(cursor, DB_NAME)
    except mysql.connector.Error as err:
        logger.error("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, DB_NAME)
            logger.info("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            logger.critical(err)
            #exit(1)
    else:
        logger.debug("Database Exists?")
    cursor.close()
    cnx = connect_central_management()
    cursor = cnx.cursor()
    for table in TABLES:
        create_table(cursor, table, TABLES[table])

def check_for_database(cursor, DB_NAME: str) -> bool:
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except:
        return False
    return True

def create_database(cursor, DB_NAME: str):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        logger.critical("Failed creating database: {}".format(err))
        #exit(1)

def create_table(cursor, table_name, table_description):
    try:
        logger.info(f"Creating Table {table_name}: ")
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            logger.error(f"Table {table_name} Already Exists")
        else:
            logger.critical(err.msg)
    else:
        logger.info(f"Table {table_name} Created")
