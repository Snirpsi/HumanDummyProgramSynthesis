#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words or returns a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8000
    
    web