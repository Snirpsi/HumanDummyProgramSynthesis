#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    
    #A function that accepts a connection from the client.
    client_socket, address = server_socket.accept()
    
    #A function that prints the message received from the client.
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(data)
    
    #A function that closes the connection.
    client_socket.close()
    server_socket.close()

