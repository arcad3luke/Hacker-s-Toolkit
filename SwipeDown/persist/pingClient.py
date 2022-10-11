import socket
import SwipeDown.SwipeDown.swipedown as sd

class pingClient:
    
    Set = range(1, 255)
    port = range(0,65535)
    randomIP = f'{Set}.{Set}.{Set}.{Set}:{port}'
    url_prefix = {
        'HTTPS':'https://',
        'HTTP':'http://',
        'FTP':'ftp://',
        'SSH':'ssh://',
        'MAILTO':'mailto:'}
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((url_prefix, randomIP))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                   break
                conn.sendall(data)