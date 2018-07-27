"""Server Class"""

import random
import socket
import jacks
from .common import send_msg, recv_msg

class Server:
    """Server Class"""
    def __init__(self, port=7770, player_count=2):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), port))

        self.deck = jacks.Deck(shuffle=True)
        self.stacks = [100] * player_count
        self.players = []

        self.socket.listen(player_count)
        for player_id in range(player_count):
            player = self.socket.accept()
            self.players.append(player)
            send_msg(player[0], player_id)

        self.button = random.randint(0, player_count-1)
        self.broadcast(self.button)
        self.broadcast(self.stacks)

    def broadcast(self, msg):
        """broadcast message to all players"""
        for player in self.players:
            send_msg(player[0], msg)

    def preflop(self):
        for player in self.players:
            send_msg(player[0], self.deck.draw(2))

    def flop(self):
        self.broadcast(self.deck.draw(3))

    def turn(self):
        self.broadcast(self.deck.draw(1))

    def river(self):
        self.broadcast(self.deck.draw(1))

    def hand(self):
        self.preflop()
        self.flop()
        self.turn()
        self.river()
