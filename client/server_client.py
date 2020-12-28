#https://stackoverflow.com/questions/39498117/simple-python-telnet-client-server-example-doesnt-work
import telnetlib

HOST = '127.0.0.1'
PORT = 8008
# from pudb import set_trace; set_trace()
tn = telnetlib.Telnet(HOST, PORT)

data = tn.read_until("custom server", timeout=1)
print("Data: " + data)

tn.close()