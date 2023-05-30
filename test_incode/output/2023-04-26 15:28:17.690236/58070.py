#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port. """    
    port = 1
    while port < 65535:
        port = port + 1
        print('Port %d is open.' % port)
        
