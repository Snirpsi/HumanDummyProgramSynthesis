#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port or adds a port. """    
    
    import sys
    
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
        
        