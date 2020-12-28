import socketserver
from telnetsrv.threaded import TelnetHandler

class MyHandler(TelnetHandler):
    WELCOME = "TEST"

class TelnetServer(socketserver.TCPServer):
    allow_reuse_address = True

server = TelnetServer(("0.0.0.0","8008"), MyHandler)
server.serve_forever()