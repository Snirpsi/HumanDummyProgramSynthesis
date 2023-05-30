#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that opens a port.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    while True:
        connection, client_address = server_socket.accept()
        print("Got connection from", client_address)
        connection.sendall(b'Hello, world!')
        connection.close()

