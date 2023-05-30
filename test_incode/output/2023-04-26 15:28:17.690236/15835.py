#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers and enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    ports = [port for port in range(1,65535)]
    
    ports.remove