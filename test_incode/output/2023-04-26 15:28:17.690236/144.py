#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    import sys
    
    ports = []
    
    for port in range(1024):
        ports.append(port)
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    
    