"""common functions for client and server"""

def send_msg(socket, msg):
    """send message to player"""
    socket.send(bytes(str(msg), 'utf8'))
