"""Player Class"""

import socket
from .common import send_msg, recv_msg

class Player:
    """Player Class"""
    def __init__(self, server, port=7770):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server, port))
        self.position = recv_msg(self.socket)

    def Check(self):
        """send action to server"""
        send_msg(self.socket, 'Check')

    def Fold(self):
        """send action to server"""
        send_msg(self.socket, 'Fold')

    def Call(self):
        """send action to server"""
        send_msg(self.socket, 'Call')

    def Raise(self, amount):
        """send action to server"""
        send_msg(self.socket, 'Raise ' + str(amount))

    def Bet(self, amount):
        """send action to server"""
        send_msg(self.socket, 'Bet ' + str(amount))

    def get_button(self):
        return recv_msg(self.socket)
