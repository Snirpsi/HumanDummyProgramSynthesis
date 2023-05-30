#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that removes a port.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen(1)
    while True:
        client, addr = server.accept()
        client.settimeout(10)
        client.sendall("HTTP/1.1 200 OK\r\nServer: Apache\r\nConnection: close\r\n\r\n")
        client.close()

