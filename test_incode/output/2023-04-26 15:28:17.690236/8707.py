#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and converts words. """    
    
    import sys
    
    ports = []
    
    for port in sys.argv[1:]:
        ports.append(port)
    
    ports.sort()
    
    for port in ports:
        
        