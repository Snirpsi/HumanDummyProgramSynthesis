#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port and converts all ports. """    
    import sys
    port = int(sys.argv[1])
    
    ports = range(port, port+2)
    
    for port in ports:
        print(port)
        
