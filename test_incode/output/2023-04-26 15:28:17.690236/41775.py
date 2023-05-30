#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    
    import sys
    
    ports = []
    
    for port in sys.argv[1:]:
        ports.append(int(port))
    
    for port in ports:
        