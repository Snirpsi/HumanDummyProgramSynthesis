#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or prints a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
        
        