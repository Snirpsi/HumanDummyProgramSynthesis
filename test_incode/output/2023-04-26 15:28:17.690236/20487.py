#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    
    port = 8080
    
    # Create a socket to listen for connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen()
    
    # Accept the connection and print its contents.
    connection, client_address = server_socket.accept()
    
    # Receive the request and print it.
    data = connection.recv(1024)
    print(data)
    
    # Close the connection and end the server.
    connection.close()
    server_socket.close()
    
