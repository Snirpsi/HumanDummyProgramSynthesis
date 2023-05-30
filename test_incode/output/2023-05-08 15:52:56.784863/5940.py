#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that stores a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen(5)
    while True:
        client, address = server.accept()
        print("Got connection from", address)
        client.send("Hello World!")
        client.close()

