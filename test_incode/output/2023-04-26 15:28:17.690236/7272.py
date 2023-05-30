#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports or enumerates all ports. """    
    ports = Ports()
    while True:
        ports.enumerate()
        ports.enumerate_all()
        ports.enumerate_all_ports()
        ports.enumerate_all_ports_