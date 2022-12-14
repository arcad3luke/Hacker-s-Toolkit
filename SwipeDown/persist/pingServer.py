import socket
from SwipeDown.SwipeDown.Utility.Shell import shell_server as shell


def pingServer(host = shell.HOST, port = shell.PORT):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

pingServer()
