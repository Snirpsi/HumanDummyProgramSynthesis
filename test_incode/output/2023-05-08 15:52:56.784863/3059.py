#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that iterates over a port.
    #The port is passed as a parameter.
    #The port is then opened and listened for connections.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen(5)
    while True:
        client, addr = server.accept()
        print("Got connection from", addr)
        client.sendall("Hello, world!")
        client.close()

