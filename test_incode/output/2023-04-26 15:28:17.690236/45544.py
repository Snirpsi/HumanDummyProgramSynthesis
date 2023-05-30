#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port or stores words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port > 0 and port < 65536:
            