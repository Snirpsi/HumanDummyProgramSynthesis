#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or prints a port. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    