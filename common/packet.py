class Packet:
    type = ""
    data = ""

    def __init__(self, type: str, data: str):
        self.type = type
        self.data = data

    def __str__(self) -> str:
        return f"{self.type}|{self.data}"

    def __bytes__(self) -> bytes:
        return self.__str__().encode()

def build_packet_from_str(string: str) -> Packet:
    split = string.split("|")
    return Packet(split[0], split[1])