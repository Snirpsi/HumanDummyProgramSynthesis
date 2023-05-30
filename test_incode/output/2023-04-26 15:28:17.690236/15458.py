#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port. """    
    port = 0
    while port < 65535:
        port = port + 1
        print('Port #' + str(port))
        
