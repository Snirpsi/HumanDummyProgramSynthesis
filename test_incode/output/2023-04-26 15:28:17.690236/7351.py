#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports. """    
    
    import sys
    
    ports = enumerate_ports()
    
    for port in ports:
        print(port)
    
    sys.exit(0)
    
