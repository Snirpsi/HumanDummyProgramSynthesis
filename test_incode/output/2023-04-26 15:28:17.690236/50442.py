#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port and iterates over a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    ports = [int(i) for i in sys.argv[2:]]
    
    ports_