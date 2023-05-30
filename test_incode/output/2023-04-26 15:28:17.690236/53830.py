#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers or multiplyes all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports = list(map(lambda x: x*