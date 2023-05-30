#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or multiplyes a port. """    
    
    port = sys.argv[1]
    
    if port == 'open':
        open