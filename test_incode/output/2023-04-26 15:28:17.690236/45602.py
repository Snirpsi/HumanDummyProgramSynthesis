#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or removes a port. """    
    
    ports = [int(x) for x in sys.argv[1:]]
    
    for port in ports:
        
        