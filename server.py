import socket
from libs import check

print('=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=')
print('|    \033[91mC \033[93mO \033[91mN \033[93mN \033[91mE \033[93mC \033[91mT    \033[93mF \033[91mO \033['
      '93mU \033[91mR\033[0m    |')
print('|       Created by Patrick       |')
print('|             v0.2.0             |')
print('|                                |')
print('|             SERVER             |')
print('|                                |')
print('|           Starting...          |')
print('|                                |')
print('=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=')
player_count = 0
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
port = check.get_port_select()
hostname = socket.gethostname()
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print()
print()
print()
print()
print()
print(f'=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=')
print(f'|    \033[91mC \033[93mO \033[91mN \033[93mN \033[91mE \033[93mC \033[91mT    \033[93mF \033[91mO \033['
      '93mU \033[91mR\033[0m    |')
print(f'|       Created by Patrick       |')
print(f'|             v0.2.0             |')
print(f'|                                |')
print(f'|             SERVER             |')
print(f'|                                |')
print(f'            {hostname}            ')
print(f'              {port}              ')
print(f'=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=')
serv.bind((hostname, port))
serv.listen(5)
print('Server Started...')
while True:
      conn, addr = serv.accept()
      from_client = ''
      while True:
            data = conn.recv(4096)
            if not data: break
            from_client += data.decode('utf8')
            print(from_client)
            conn.send(board.encode())
print('client disconnected and shutdown')