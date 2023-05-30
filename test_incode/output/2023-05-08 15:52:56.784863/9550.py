#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that opens a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(1)
    while True:
        client, addr = server.accept()
        print("Connected by", addr)
        client.sendall(b'Hello, world!')
        client.close()

