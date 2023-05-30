#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports and iterates over fruits. """    
    
    ports = openports()
    
    while True:
        for port in ports:
            