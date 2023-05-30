#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port or enumerates a port. """    
    ports = Ports()
    while True:
        ports.enumerate()
        ports.remove_port()
        ports.