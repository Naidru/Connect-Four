import socket
from libs import check


def multiplayer_client():
    """
    Join a match
    """
    port = check.get_port_select()
    hostname = socket.gethostname()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((hostname, port))
    client.send("I am CLIENT\n".encode())
    # Define the initial variables
    red = '\033[91m⬤\033[0m'
    yellow = '\033[93m⬤\033[0m'
    winner = False
    empty = '\033[92m〇\033[0m'
    turn = red
    board = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty]
    ]
    from_server = client.recv(4096)
    print(from_server.decode())




