#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port or returns all ports. """    
    ports = listPorts()
    while True:
        ports.remove('