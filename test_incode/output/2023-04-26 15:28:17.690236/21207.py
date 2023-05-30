#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or enumerates all ports. """    
    port = 0
    
    while True:
        port = port + 1
        print('serving on port ' + str(port))
        
        