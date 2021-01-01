from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
import main

# Dict Def: {"mac:address": {pub:"", sessionpub:"", sessionpriv: ""}
from Crypto.PublicKey.RSA import RsaKey

if main.side == "server":
    known_clients = dict()

our_pub = ""
our_priv = "~/.ssh/id_rsa"

if main.side == "client":
    session_pub = ""
    session_priv = ""

# Returns SessionPub. We log the SessionPriv.

def set_session(mac: str, pub_key: str):
    if main.side == "client":
        global session_pub
        session_pub = pub_key
    elif main.side == "server":
        known_clients[mac]["sessionpub"] = pub_key

def create_session(mac: str) -> str:
    if main.side == "client":
        global session_priv
        global session_pub
    priv_key = RSA.generate(4096)
    pub_key = priv_key.publickey()
    if main.side == "server":
        known_clients[mac][f"{main.side}_sessionpriv"] = priv_key.export_key().decode()
    if main.side == "client":
        session_priv = priv_key.export_key().decode()
    return pub_key.export_key().decode()

if main.side == "server":
    def add_known(mac: str, client_pub: str):
        known_clients[mac]["clientpub"] = client_pub


def encrypt(message: str, pub_key: str) -> str:
    pub = RSA.import_key(pub_key)
    cipher = PKCS1_OAEP.new(key=pub)
    return cipher.encrypt(message.encode()).decode()


def decrypt(message: bytes, priv_key: str) -> str:
    priv = RSA.import_key(priv_key)
    cipher = PKCS1_OAEP.new(key=priv)
    return cipher.decrypt(message).decode()


def session_encrypt(message: str) -> str:
    if main.side == "client":
        return encrypt(message, session_pub)
    if main.side == "server":
        return encrypt(message, )