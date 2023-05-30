#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports or converts a port. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 0:
        print("Usage: python3 -m port