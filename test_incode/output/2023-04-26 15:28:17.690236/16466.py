#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or enumerates a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '80'
    
    webserver