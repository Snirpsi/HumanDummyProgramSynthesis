#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers or enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    ports = [