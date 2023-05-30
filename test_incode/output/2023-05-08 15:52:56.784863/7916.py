#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that removes a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen(1)
    while True:
        client, address = server.accept()
        print("Got connection from %s" % address)
        client.close()

