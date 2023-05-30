#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports or adds a list of words. """    
    import sys
    ports = sys.argv[1:]
    ports = ports.split(',')
    ports = ports.