#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that adds a port.
    while True:
        port = port + 1
        server = socketserver.TCPServer(("", port), MyHandler)
        server.serve_forever()

