#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers or opens all ports. """    
    while True:
        ports = find_ports()
        for port in ports:
            