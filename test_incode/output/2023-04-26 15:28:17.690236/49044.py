#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    
    # Open a socket to listen for connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(1)
    
    # Accept a connection and print its contents.
    connection, client_address = server_socket.accept()
    
    # Receive the request and print its contents.
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print(data)
        connection.send(data)
    
    # Close the connection.
    connection.close()
    
    # Close the socket.
    server_socket.close()
    
