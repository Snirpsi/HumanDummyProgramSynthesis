#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports. """    
    while True:
        ports = [int(p) for p in sys.argv[1:]]
        for port in ports:
            port = int(port)
            