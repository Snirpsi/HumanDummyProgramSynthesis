#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that opens a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen(1)
    client, address = server.accept()
    print("Got connection from", address)
    while True:
        data = client.recv(1024)
        if not data:
            break
        client.send(data)
    client.close()

