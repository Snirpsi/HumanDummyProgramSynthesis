#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that adds a port.
    while True:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("", port))
        server.listen(1)
        client, addr = server.accept()
        print("Got connection from", addr)
        client.sendall("Hello World!")
        client.close()
        server.close()

