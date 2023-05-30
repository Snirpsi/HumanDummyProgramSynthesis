#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports or multiplyes a port. """    
    
    ports = sys.argv[1:]
    
    for port in ports:
        print(port