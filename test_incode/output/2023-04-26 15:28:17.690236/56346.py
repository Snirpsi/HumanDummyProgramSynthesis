#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports or removes a port. """    
    
    ports = PortEnumerator()
    ports.enumerate_ports()
    
    ports.remove