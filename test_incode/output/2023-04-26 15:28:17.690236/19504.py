#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and opens all ports. """    
    
    ports = range(65535)
    for port in ports:
        open