#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port. """    
    port = int(sys.argv[1])
    
    # Create a socket and bind to port 8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    # Accept the connection and then 