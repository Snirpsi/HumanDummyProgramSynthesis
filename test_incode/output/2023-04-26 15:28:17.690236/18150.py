#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    import sys
    ports = [int(x) for x in sys.argv[1:]]
    ports = list(set(ports))
    ports.sort()
    
    for port in ports:
        