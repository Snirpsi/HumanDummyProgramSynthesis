#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    import sys
    
    ports = [int(i) for i in sys.argv[1:]]
    
    ports_converted = [port