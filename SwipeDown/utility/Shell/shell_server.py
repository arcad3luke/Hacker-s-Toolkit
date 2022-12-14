#!/bin/env/python3

import socketserver

global HOST, PORT

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data)

if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9999
    try:
        with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
            server.serve_forever()
    except KeyboardInterrupt or IOError:
        server.shutdown()