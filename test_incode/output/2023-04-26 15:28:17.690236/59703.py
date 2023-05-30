#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports and converts a port. """    
    
    ports = Ports()
    
    for port in ports.ports:
        port.convert(