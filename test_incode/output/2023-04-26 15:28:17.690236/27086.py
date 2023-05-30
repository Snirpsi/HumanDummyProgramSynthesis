#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports and converts a port. """    
    ports = range(1,65535)
    for port in ports:
        ports[port] = ports[port]*