#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers and opens all ports. """    
    import sys
    
    ports = [int(i) for i in sys.argv[1:]]
    
    for port in ports:
        