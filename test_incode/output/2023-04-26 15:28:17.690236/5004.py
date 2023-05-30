#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    
    import sys
    
    ports = [int(x) for x in sys.argv[1:]]
    
    for port in ports:
        
        