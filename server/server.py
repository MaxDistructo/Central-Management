import socketserver
from telnetsrv.threaded import TelnetHandler

class MyHandler(TelnetHandler):
    WELCOME = "TEST"

class TelnetServer(socketserver.TCPServer):
    allow_reuse_address = True

server = TelnetServer(("0.0.0.0","8008"), MyHandler)
server.serve_forever()

class DB_Connection():
    def __init__(self, ip, port, username, password):
        print("unimplemented")
    def connect(self):
        print("unimplemented")

class DB_Server():
    def __init__(self):
        print("unimplemented")
    def start(self):
        print("unimplemented")