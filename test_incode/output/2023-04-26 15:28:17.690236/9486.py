#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = ['hello', 'world', '