#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that requests a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen()
    client, addr = server.accept()
    print("Got connection from ", addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        client.send(data)
    server.close()

