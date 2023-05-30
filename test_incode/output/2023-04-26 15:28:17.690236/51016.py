#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers and returns a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server