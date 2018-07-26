"""Server Class"""

import random
import socket
import jacks
from .common import send_msg

class Server:
    """Server Class"""
    def __init__(self, port=7770, player_count=2):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), self.port))
        self.deck = jacks.Deck(shuffle=True)

        self.players = []
        self.socket.listen(player_count)

        for player_id in range(player_count):
            player = self.socket.accept()
            self.players.append(player)
            send_msg(player[0], player_id)

        button = random.randint(0, player_count-1)
        small_blind = str((button + 1) % player_count)
        big_blind = str((button + 2) % player_count)
        self.broadcast(str(button) + ' ' + small_blind + ' ' + big_blind)

    def broadcast(self, msg):
        """broadcast message to all players"""
        for player in self.players:
            send_msg(player[0], msg)

    def deal_hole_cards(self):
        """deal hole cards to all players"""
        for player in self.players:
            send_msg(player[0], self.deck.draw(2))

    def deal_flop(self):
        """deal flop"""
        self.broadcast(self.deck.draw(3))

    def deal_turn(self):
        """deal turn"""
        self.broadcast(self.deck.draw(1))

    def deal_river(self):
        """deal river"""
        self.broadcast(self.deck.draw(1))
