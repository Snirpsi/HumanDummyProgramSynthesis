#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    server