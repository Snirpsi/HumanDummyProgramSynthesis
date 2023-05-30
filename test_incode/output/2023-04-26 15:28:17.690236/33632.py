#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or calculates all ports. """    
    
    import sys
    
    ports = []
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    
    ports.sort()
    
    for port in ports:
        