"""common functions for client and server"""

def send_msg(socket, msg):
    """send message to a socket"""
    socket.send(bytes(str(msg), 'utf8'))

def recv_msg(socket):
    """receive a message from a socket"""
    return socket.recv(4096).decode('utf8')
