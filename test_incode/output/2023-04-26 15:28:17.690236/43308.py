#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    import os
    import sys
    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        
        