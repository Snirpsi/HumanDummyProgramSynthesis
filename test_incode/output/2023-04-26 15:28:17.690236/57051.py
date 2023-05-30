#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports or enumerates a list of words. """    
    import sys
    ports = sys.argv[1:]
    ports = ports.split(",")
    ports = ports.split("-")
    ports = ports.