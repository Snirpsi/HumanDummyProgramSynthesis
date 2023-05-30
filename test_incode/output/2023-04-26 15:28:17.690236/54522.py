#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port or iterates over a port. """    
    
    port = int(sys.argv[1])
    
    # Open a port if port is given
    if port > 0:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', port))
        server_socket.listen(5)
        print('Listening on port {}'.format(port))
        
    # Iterate over all open ports
    else:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 0))
        server_socket.listen(5)
        print('Listening on port 0')
        
    while True:
        connection, client_address = server_socket.accept()
        print('Connected by', client_address)
        
        # Send the message to the client
        connection.send('Hello World!')
        
        # Close the connection
        connection.close()
        
        # Wait for the next message
        connection.send('