#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words or converts all ports. """    
    import sys
    ports = sys.argv[1:]
    ports = ports.split(',')
    ports = ports.