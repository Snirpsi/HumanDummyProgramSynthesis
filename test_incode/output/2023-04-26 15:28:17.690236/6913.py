#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or prints user input. """    
    port = int(sys.argv[1])
    
    # Open a socket to listen for incoming connections.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    while True:
        # Accept a connection and 