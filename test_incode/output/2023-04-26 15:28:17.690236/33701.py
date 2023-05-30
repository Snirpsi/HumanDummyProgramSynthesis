#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and stores all ports. """    
    ports = Ports()
    ports.convert_ports(sys.argv[1])
    ports.store_ports()

<|/ file filename=ports.py |>