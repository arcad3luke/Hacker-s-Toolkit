import socket

def pingClient(Set = range(1,255), port = range(1,65535)):
    IP = f'{Set}.{Set}.{Set}.{Set}:{port}'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(IP)
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                   break
                conn.sendall(data)
        with open('target.json', 'w') as f:
            f.writelines(data)
pingClient()