#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    
    #A function that accepts a connection and then prints it.
    while True:
        connection, client_address = server_socket.accept()
        print('Connection from', client_address)
        connection.sendall(b'Hello, world!')
        connection.close()

