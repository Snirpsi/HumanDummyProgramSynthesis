#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and prints a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '8080'
    
    web