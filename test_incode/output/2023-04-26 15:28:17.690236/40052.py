#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and adds words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = ['hello', 'world', '