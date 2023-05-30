#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    while True:
        ports.reverse()
        
        for port in ports:
            