#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and opens a list of words. """    
    
    port = sys.argv[1]
    
    words = []
    
    # Open a socket to listen on port and accept connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    
    while True:
        connection, address = sock.accept()
        
        # Accept a connection and read its data
        data = connection.recv(1024)
        
        # Process the data received from the client
        words = words.