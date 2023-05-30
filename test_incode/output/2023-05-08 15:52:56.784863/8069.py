#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that adds a port.
    #This program will listen for connections on port 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen(1)
    while True:
        client, addr = server.accept()
        print("Got connection from", addr)
        client.sendall("Hello World!")
        client.close()

