#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or stores numbers. """    
    port = int(sys.argv[1])
    
    if port == 0: 
        port = 1
    
    