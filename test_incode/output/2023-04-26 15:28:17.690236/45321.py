#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and opens all ports. """    
    
    ports = [int(i) for i in sys.argv[1:]]
    
    for port in ports:
        