#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen()
    print("Listening on port " + str(port))
    while True:
        client, addr = server.accept()
        print("Connected by", addr)
        client.sendall("Hello, world!")
        client.close()

