#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports and prints a port. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    for port in ports:
        