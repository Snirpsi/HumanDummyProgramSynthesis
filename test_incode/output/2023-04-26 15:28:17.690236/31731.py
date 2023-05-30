#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    
    ports = []
    
    # Create a TCP server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    server.bind(('localhost', 0))
    
    # Listen for incoming connections
    server.listen(1)
    
    # Accept connections
    while True:
        # Wait for a connection
        connection, address = server.accept()
        
        # Send the address and port to the client
        connection.sendto('