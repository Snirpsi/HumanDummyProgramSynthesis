#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and adds numbers. """    
    
    ports = []
    
    # Open a socket to listen for connections.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    sock.bind(('localhost', 0))
    
    # Listen for incoming connections
    sock.listen(10)
    
    # Accept the incoming connection and print its port number
    while True:
        connection, client_address = sock.accept()
        
        # Send the port number back to the client
        connection.sendall('