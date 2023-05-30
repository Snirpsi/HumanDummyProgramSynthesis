#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and stores a list of words. """    
    port = int(sys.argv[1])
    words = []
    
    # Open a socket to the port and listen for connections.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    
    # Accept the connection and store a reference to the client socket
    # in our word list.
    while True:
        connection, address = sock.accept()
        words.append(connection.recv(1024))
        
        # Close the connection and end the loop.
        connection.close()
        
        # Wait for another client connection.
        connection.