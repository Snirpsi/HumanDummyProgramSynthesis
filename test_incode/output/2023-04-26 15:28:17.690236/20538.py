#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    
    # Open a socket and listen for connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 8080))
    server_socket.listen(1)
    
    # Accept a connection and print its contents.
    while True:
        connection, client_address = server_socket.accept()
        print('Client connected:', client_address)
        
        # Read all data from the client and send it to the server.
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)
        
        # Close the connection when finished.
        connection.close()
        
    # Close the socket.
    server_socket.close()
