#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port or adds a port. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 9999
    
    