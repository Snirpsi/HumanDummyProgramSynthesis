#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers. """    
    
    numbers = []
    
    # Open a socket to listen for connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(1)
    
    # Accept a connection and then start listening for new connections.
    while True:
        connection, client_address = server_socket.accept()
        
        # Receive the number from the client.
        number = connection.recv(1024).decode('utf-8')
        
        # Add the number to the list.
        numbers.append(number)
        
        # Send the number back to the client.
        connection.send(number.encode('utf-8'))
        
        # Close the connection.
        connection.close()
    
    # Close the server socket.
    server_socket.close()
    
    # Print the list.
    print('\n'.join(numbers))
    
    # Close the socket.
    server_socket.close()
    
    # Run the 