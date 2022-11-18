import socket


def pingServer(host='localhost', port=65432):
    ip = f'{host}:{port}'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(ip)
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