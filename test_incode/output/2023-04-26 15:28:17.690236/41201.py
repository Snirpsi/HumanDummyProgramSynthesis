#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports and iterates over all ports. """    
    
    ports = range(0,65535)
    while True:
        for port in ports:
            