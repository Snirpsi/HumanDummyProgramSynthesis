#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        print("Connected by", addr)
        client.sendall("Hello, world!".encode())
        client.close()

