from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import socket

from common.packet import Packet

peer_pub = ""
our_priv = ""
our_pub = ""


def __init__():
    try:
        with open('pub.pem', 'r') as f:
            our_pub = f.read()
        with open('priv.pem', 'r') as f:
            our_priv = f.read()
    except:
        generate()


def generate():
    global our_priv
    global our_pub

    priv = RSA.generate(4096)
    our_priv = priv.export_key().decode()

    pub = priv.publickey()
    our_pub = pub.export_key().decode()

    with open('private.pem', 'w') as f:
        f.write(our_priv)

    with open('public.pem', 'w') as f:
        f.write(our_pub)


def encrypt(message: str) -> str:
    pub = RSA.import_key(peer_pub)
    cipher = PKCS1_OAEP.new(key=pub)
    return cipher.encrypt(message.encode()).decode()


def decrypt(message: str) -> str:
    peer = RSA.import_key(our_priv)
    cipher = PKCS1_OAEP.new(key=peer)
    return cipher.decrypt(message.encode()).decode()


def negotiate(peer_ip: str, port):
    global peer_pub
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = (peer_ip, port)
    s.connect(server)
    s.sendall(Packet("pubkey", our_pub).__bytes__())
    peer_pub = s.recv(8196)
    s.close()