"""Player Class"""

import socket

class Player:
    """Player Class"""
    def __init__(self, server, port=7770):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server, port))
        self.position = self.receive()

    def receive(self):
        return self.socket.recv(4096).decode('utf8')
