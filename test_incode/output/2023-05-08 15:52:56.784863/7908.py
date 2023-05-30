#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that requests a port.
    #The port is then used to start a server.
    #The server then listens for connections.
    #The client then connects to the server.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(1)
    while True:
        client, address = server.accept()
        print('Connected by', address)
        data = client.recv(1024)
        client.send(data)
        client.close()

