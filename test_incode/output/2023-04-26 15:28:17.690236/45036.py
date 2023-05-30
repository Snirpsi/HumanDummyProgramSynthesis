#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words or prints all ports. """    
    import sys
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        
        