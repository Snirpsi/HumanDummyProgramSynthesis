#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or returns all ports. """    
    ports = Ports()
    while True:
        ports.print_ports()
        ports.print_all_ports()
        ports.print_all_ports_