#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports = list(map(lambda x: x*