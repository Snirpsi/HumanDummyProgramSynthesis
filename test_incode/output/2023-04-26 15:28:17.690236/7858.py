#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    import sys
    ports = list(range(0,65535))
    ports.sort()
    for port in ports:
        sys.stdout.write('