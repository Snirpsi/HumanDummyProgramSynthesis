#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    # Open a socket to listen for connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(1)
    
    # Accept the connection and send it to the client
    connection, client_address = server_socket.accept()
    
    # Receive the message and print it to the client
    message = connection.recv(1024)
    connection.close()
    
    # Send the message back to the client
    connection.send(message)
    
    # Close the connection
    connection.close()
    
    # Close the server
    server_socket.close()
    
