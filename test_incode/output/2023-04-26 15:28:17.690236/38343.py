#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port or multiplyes all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    
    # Add ports
    for p in ports:
        ports.append(p+