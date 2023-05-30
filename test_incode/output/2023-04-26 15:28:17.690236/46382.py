#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers and opens all ports. """    
    while True:
        ports = openports()
        for port in ports:
            