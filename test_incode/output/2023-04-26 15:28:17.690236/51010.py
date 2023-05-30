#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and calculates a port. """    
    
    import sys
    
    port = 0
    
    for arg in sys.argv[1:]:
        
        if arg == '--port':
            port = 